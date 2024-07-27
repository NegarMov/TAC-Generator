class Identifier:

    def __init__(self, addr: int, type: str, args=None):
        self.addr = addr
        self.type = type
        if args != None:
            self.args = args
    

class Scope:

    def __init__(self, parent=None):
        self.identifiers = {}
        self.parent = parent
        self.children = []

    # Add an identifier to the scope
    def add_identifier(self, identifier_name: str, identifier: Identifier):
        if identifier_name in self.identifiers.keys():
            raise RuntimeError(f"{identifier_name} is already declared at the current scope")
        
        self.identifiers[identifier_name] = identifier


class SymbolTable:
    
    def __init__(self) -> None:
        self.root = Scope()
        
        self.current_scope = self.root
        
        self.add_identifier("printInt", -1, 'v', ['i'])
        self.add_identifier("printDouble", -1, 'v', ['d'])
        self.add_identifier("printString", -1, 'v', ['s'])
        self.add_identifier("readInt", -1, 'i', [])
        self.add_identifier("readDouble", -1, 'd', [])

    # Add an identifier to the current scope
    def add_identifier(self, identifier_name: str, addr: int, type: str, args=None):
        self.current_scope.add_identifier(identifier_name, Identifier(addr, type, args))

    # Add a scope to the symbol table
    def add_scope(self):
        scope = Scope(self.current_scope)
        self.current_scope.children.append(scope)
        self.current_scope = scope

    # Remove a scope from the symbol table
    def remove_scope(self):
        if self.current_scope.parent is None:
            raise RuntimeError("Can't remove the root scope")
        self.current_scope = self.current_scope.parent

    # Climb up the tree to find the identifier
    def find_identifier(self, identifier_name:str) -> Identifier:
        cs = self.current_scope
        while cs is not None:
            if identifier_name in cs.identifiers.keys():
                return cs.identifiers[identifier_name]
            cs = cs.parent

        raise RuntimeError(f"{identifier_name} is not declared at this scope")

    # Checks if the program has a main function
    def has_main(self) -> bool:
        if 'main' in self.root.identifiers.keys():
            return True
        
        return False
