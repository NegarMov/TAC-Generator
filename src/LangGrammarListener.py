# Generated from LangGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LangGrammarParser import LangGrammarParser
else:
    from LangGrammarParser import LangGrammarParser
from SymbolTable import SymbolTable
from colorama import Fore
import re

# This class defines a complete listener for a parse tree produced by LangGrammarParser.
class LangGrammarListener(ParseTreeListener):

    def __init__(self):
        super(LangGrammarListener,self).__init__()
        self.symbol_table = SymbolTable()
        self.top = 0
        self.bottom = 0
        self.next_label = 0
        self.next_scope = 1
        self.used_memory_stack = []
        self.func_name = ''
        self.predefined_functions = ['printInt', 'printDouble', 'printString', 'readInt', 'readDouble']
        self.code = []


    def printErr(self, error_msg):
        print(Fore.RED + "Error: " + Fore.RESET + str(error_msg))
        exit()


    def getLabel(self) -> str:
        new_label = f'L{self.next_label}'
        self.next_label += 1
        return new_label


    def printAddr(self, addr):
        match = re.search(r"\[(\d+)\]", addr)
        if match:
            number = int(match.group(1))
            if self.func_name == 'main':
                if self.top - number == 0:
                    return re.sub(r'\[\d+\]', '[top]', addr)
                else:
                    return re.sub(r'\[\d+\]', f'[top - {self.top - number}]', addr)

            else:
                if self.bottom - number == 0:
                    return re.sub(r'\[\d+\]', '[bottom]', addr)
                else:
                    return re.sub(r'\[\d+\]', f'[bottom + {self.bottom - number}]', addr)
        
        else:
            return addr


    def getIdType(self, id) -> str:
        if id.type == 'i' or id.type == 'b':
            return 'i'
        elif id.type == 'd':
            return 'd'
        elif id.type == 'v':
            return 'v'


    def flatten_array(self, arr):
        result = []
        for item in arr:
            if isinstance(item, list):
                result.extend(self.flatten_array(item))
            else:
                result.append(item)
        return result


    # Enter a parse tree produced by LangGrammarParser#prog.
    def enterProg(self, ctx:LangGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#prog.
    def exitProg(self, ctx:LangGrammarParser.ProgContext):
        if not self.symbol_table.has_main():
            self.printErr(f"The program has no main function")

        ctx.code = [self.code[-1]] + self.code[:-1]
        ctx.code = "\n".join([f for f in ctx.code])
        ctx.code += '\n\nmain_end:'
        ctx.code = "\n".join(["\t" + line for line in ctx.code.splitlines()])

        with open("template_start.txt", "r") as start_file:
            template_start = start_file.read()

        with open("template_end.txt", "r") as end_file:
            template_end = end_file.read()

        with open("IRcode.c", "w") as output_file:
            output_file.write(template_start + ctx.code + template_end)


    # Enter a parse tree produced by LangGrammarParser#func_list.
    def enterFunc_list(self, ctx:LangGrammarParser.Func_listContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#func_list.
    def exitFunc_list(self, ctx:LangGrammarParser.Func_listContext):
        ctx.code = ctx.func_def().code
        
        if ctx.func_list():
            ctx.code += '\n' + ctx.func_list().code


    # Enter a parse tree produced by LangGrammarParser#func_def.
    def enterFunc_def(self, ctx:LangGrammarParser.Func_defContext):
        self.func_name = ctx.ID().getText()
        
        ctx.arg_types = []

        ctx.type = 'v' if ctx.DATA_TYPE().getText() == 'void' else \
            'i' if ctx.DATA_TYPE().getText() == 'int' else \
                'd' if ctx.DATA_TYPE().getText() == 'double' else 'b'

        self.used_memory_stack.append(0)

    # Exit a parse tree produced by LangGrammarParser#func_def.
    def exitFunc_def(self, ctx:LangGrammarParser.Func_defContext):
        self.symbol_table.remove_scope()

        ctx.code = f'\n{ctx.ID().getText()}:'
        ctx.code += ctx.code_block().code
        if self.func_name != 'main':
            ctx.code += f'\n{ctx.ID().getText()}_end:'
            ctx.code += f'\ngoto *(m[top].l);' 

        self.code.append(ctx.code)


    # Enter a parse tree produced by LangGrammarParser#param_list.
    def enterParam_list(self, ctx:LangGrammarParser.Param_listContext):
        ctx.arg_types = []

    # Exit a parse tree produced by LangGrammarParser#param_list.
    def exitParam_list(self, ctx:LangGrammarParser.Param_listContext):
        func_def = ctx.parentCtx
        
        func_def.arg_types.append(ctx.arg_types)

        if hasattr(func_def, 'ID'):
            try:
                self.symbol_table.add_identifier(func_def.ID().getText(), -1, func_def.type, func_def.arg_types)
            except Exception as e:
                self.printErr(e)

            self.symbol_table.add_scope()


    # Enter a parse tree produced by LangGrammarParser#param.
    def enterParam(self, ctx:LangGrammarParser.ParamContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#param.
    def exitParam(self, ctx:LangGrammarParser.ParamContext):
        if self.func_name == 'main':
            self.printErr("The main function accepts no parameters")
        
        if ctx.DATA_TYPE().getText() == 'void':
            self.printErr("Identifiers cannot have void data type")

        dataType = 'd' if ctx.DATA_TYPE().getText() == 'double' else \
            'i' if ctx.DATA_TYPE().getText() == 'int' else 'b'

        try:
            self.symbol_table.add_identifier(ctx.ID().getText(), self.bottom, dataType)
        except Exception as e:
            self.printErr(e)

        self.bottom += 1
        self.used_memory_stack[-1] += 1

        ctx.type = dataType

        ctx.parentCtx.arg_types.append(ctx.type)


    # Enter a parse tree produced by LangGrammarParser#code_block.
    def enterCode_block(self, ctx:LangGrammarParser.Code_blockContext):
        self.symbol_table.add_scope()

    # Exit a parse tree produced by LangGrammarParser#code_block.
    def exitCode_block(self, ctx:LangGrammarParser.Code_blockContext):
        ctx.code = ctx.stmt_list().code
        self.symbol_table.remove_scope()


    # Enter a parse tree produced by LangGrammarParser#stmt_list.
    def enterStmt_list(self, ctx:LangGrammarParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#stmt_list.
    def exitStmt_list(self, ctx:LangGrammarParser.Stmt_listContext):
        if ctx.stmt():
            ctx.code = ctx.stmt().code + ctx.stmt_list().code
        
        else:
            ctx.code = ''


    # Enter a parse tree produced by LangGrammarParser#stmt.
    def enterStmt(self, ctx:LangGrammarParser.StmtContext):
        if ctx.parentCtx.getChild(0).getText() == 'if':
            self.symbol_table.add_scope()

    # Exit a parse tree produced by LangGrammarParser#stmt.
    def exitStmt(self, ctx:LangGrammarParser.StmtContext):
        ctx.code = ctx.getChild(0).code

        if ctx.parentCtx.getChild(0).getText() == 'if':
            self.symbol_table.remove_scope()   


    # Enter a parse tree produced by LangGrammarParser#decide_with_else.
    def enterDecide_with_else(self, ctx:LangGrammarParser.Decide_with_elseContext):
        if ctx.DATA_TYPE():
            if ctx.DATA_TYPE().getText() == 'void':
                self.printErr("Identifiers cannot have void data type")

            ctx.type = 'd' if ctx.DATA_TYPE().getText() == 'double' else \
                'i' if ctx.DATA_TYPE().getText() == 'int' else 'b'

        if ctx.parentCtx.getChild(0).getText() == 'if':
            self.symbol_table.add_scope()

    # Exit a parse tree produced by LangGrammarParser#decide_with_else.
    def exitDecide_with_else(self, ctx:LangGrammarParser.Decide_with_elseContext):
        if ctx.getChild(0).getText() == 'if':
            ctx.code = ctx.expr().code
            else_label = self.getLabel()
            ctx.code += f'\nif ({self.printAddr(ctx.expr().addr)} == 0) goto {else_label};'
            ctx.code += ctx.decide_with_else(0).code
            end_label = self.getLabel()
            ctx.code += f'\ngoto {end_label};'
            ctx.code += f'\n{else_label}:'
            ctx.code += ctx.decide_with_else(1).code
            ctx.code += f'\n{end_label}:'

        elif ctx.code_block():
            ctx.code = ctx.code_block().code

        elif ctx.DATA_TYPE():
            ctx.code = ctx.var_list().code

        elif ctx.ID():
            try:
                identifier = self.symbol_table.find_identifier(ctx.ID().getText())
            except Exception as e:
                self.printErr(e)

            ctx.addr = f"m[{identifier.addr}].{self.getIdType(identifier)}"
            
            ctx.type = identifier.type
            
            if ctx.getChild(1).getText() == '=':
                if identifier.type != ctx.expr().type:
                    self.printErr(f"Types mismatch on the assignment ({identifier.type}, {ctx.expr().type})")

                ctx.code = ctx.expr().code
                ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.expr().addr)};'

            elif ctx.getChild(1).getText() == '++':
                ctx.code = f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.addr)} + 1;'

            else:
                ctx.code = f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.addr)} - 1;'

        elif ctx.getChild(0).getText() == 'return':
            try:
                func_def = self.symbol_table.find_identifier(self.func_name)
            except Exception as e:
                self.printErr(e)

            if ctx.expr():
                if func_def.type != ctx.expr().type:
                    self.printErr("return type mismatch with the function signature")

                ctx.code = ctx.expr().code
                ctx.code += f'\nm[top].{self.getIdType(ctx.expr())} = {self.printAddr(ctx.expr().addr)};'
                used_memory = self.used_memory_stack.pop()
                ctx.code += f'\nbottom += {used_memory}'
                self.bottom -= used_memory
                ctx.code += f'\ngoto {self.func_name}_end;'

            else:
                if func_def.type != 'v':
                    self.printErr("non-void function must return a parameter")

                used_memory = self.used_memory_stack.pop()
                ctx.code = f'\nbottom += {used_memory}'
                self.bottom -= used_memory
                ctx.code += f'\ngoto {self.func_name}_end;'

        elif ctx.loop_stmt():
            ctx.code = ctx.loop_stmt().code

        elif ctx.expr:
            ctx.code = ctx.expr().code

        if ctx.parentCtx.getChild(0).getText() == 'if':
            self.symbol_table.remove_scope()


    # Enter a parse tree produced by LangGrammarParser#decide_no_else.
    def enterDecide_no_else(self, ctx:LangGrammarParser.Decide_no_elseContext):
        if ctx.parentCtx.getChild(0).getText() == 'if':
            self.symbol_table.add_scope()

    # Exit a parse tree produced by LangGrammarParser#decide_no_else.
    def exitDecide_no_else(self, ctx:LangGrammarParser.Decide_no_elseContext):
        if ctx.stmt():
            ctx.code = ctx.expr().code
            end_label = self.getLabel()
            ctx.code += f'\nif ({self.printAddr(ctx.expr().addr)} == 0) goto {end_label};'
            ctx.code += ctx.stmt().code
            ctx.code += f'\n{end_label}:'

        else:
            ctx.code = ctx.expr().code
            else_label = self.getLabel()
            ctx.code += f'\nif ({self.printAddr(ctx.expr().addr)} == 0) goto {else_label};'
            ctx.code += ctx.decide_with_else().code
            end_label = self.getLabel()
            ctx.code += f'\ngoto {end_label};'
            ctx.code += f'\n{else_label}:'
            ctx.code += ctx.decide_no_else().code
            ctx.code += f'\n{end_label}:'

        if ctx.parentCtx.getChild(0).getText() == 'if':
            self.symbol_table.remove_scope()


    # Enter a parse tree produced by LangGrammarParser#loop_stmt.
    def enterLoop_stmt(self, ctx:LangGrammarParser.Loop_stmtContext):
        self.symbol_table.add_scope()

    # Exit a parse tree produced by LangGrammarParser#loop_stmt.
    def exitLoop_stmt(self, ctx:LangGrammarParser.Loop_stmtContext):
        if ctx.getChild(0).getText() == 'while':
            start_label = self.getLabel()
            end_label = self.getLabel()
            ctx.code = f'\n{start_label}:'
            ctx.code += ctx.expr().code
            ctx.code += f'\nif ({self.printAddr(ctx.expr().addr)} == 0) goto {end_label};'
            ctx.code += ctx.stmt().code
            ctx.code += f'\ngoto {start_label};'
            ctx.code += f'\n{end_label}:'

        elif ctx.getChild(0).getText() == 'do':
            start_label = self.getLabel()
            end_label = self.getLabel()
            ctx.code = f'\n{start_label}:'
            ctx.code += ctx.stmt().code
            ctx.code += ctx.expr().code
            ctx.code += f'\nif ({self.printAddr(ctx.expr().addr)} > 0) goto {start_label};'

        else:
            ctx.code = ctx.init_stmt().code
            start_label = self.getLabel()
            end_label = self.getLabel()
            ctx.code += f'\n{start_label}:'
            ctx.code += ctx.expr().code
            ctx.code += f'\nif ({self.printAddr(ctx.expr().addr)} == 0) goto {end_label};'
            ctx.code += ctx.stmt().code
            ctx.code += ctx.post_stmt().code
            ctx.code += f'\ngoto {start_label};'
            ctx.code += f'\n{end_label}:'

        self.symbol_table.remove_scope()


    # Enter a parse tree produced by LangGrammarParser#init_stmt.
    def enterInit_stmt(self, ctx:LangGrammarParser.Init_stmtContext):
        pass


    # Exit a parse tree produced by LangGrammarParser#init_stmt.
    def exitInit_stmt(self, ctx:LangGrammarParser.Init_stmtContext):
        if ctx.DATA_TYPE():
            if ctx.DATA_TYPE().getText() == 'void':
                self.printErr("Identifiers cannot have void data type")

            dataType = 'd' if ctx.DATA_TYPE().getText() == 'double' else \
                'i' if ctx.DATA_TYPE().getText() == 'int' else 'b'

            try:
                if self.func_name == 'main':
                    self.symbol_table.add_identifier(ctx.ID().getText(), self.top, dataType)
                else:
                    self.symbol_table.add_identifier(ctx.ID().getText(), self.bottom, dataType)
            except Exception as e:
                self.printErr(e)

        if ctx.ID():
            try:
                identifier = self.symbol_table.find_identifier(ctx.ID().getText())
            except Exception as e:
                self.printErr(e)
            
            ctx.addr = f'm[{identifier.addr}].{self.getIdType(identifier)}'
            
            ctx.type = identifier.type

            if identifier.type != ctx.expr().type:
                self.printErr(f"Types mismatch on the assignment ({identifier.type}, {ctx.expr().type})")
            
            ctx.code = ctx.expr().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.expr().addr)};'
        
        if ctx.DATA_TYPE():
            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1


    # Enter a parse tree produced by LangGrammarParser#post_stmt.
    def enterPost_stmt(self, ctx:LangGrammarParser.Post_stmtContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#post_stmt.
    def exitPost_stmt(self, ctx:LangGrammarParser.Post_stmtContext):
        if ctx.ID():
            try:
                identifier = self.symbol_table.find_identifier(ctx.ID().getText())
            except Exception as e:
                self.printErr(e)

            ctx.addr = f"m[{identifier.addr}].{self.getIdType(identifier)}"
            
            ctx.type = identifier.type
            
            if ctx.getChild(1).getText() == '=':
                if identifier.type != ctx.expr().type:
                    self.printErr(f"Types mismatch on the assignment ({identifier.type}, {ctx.expr().type})")

                ctx.code = ctx.expr().code
                ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.expr().addr)};'

            elif ctx.getChild(1).getText() == '++':
                ctx.code = f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.addr)} + 1;'

            else:
                ctx.code = f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.addr)} - 1;'


    # Enter a parse tree produced by LangGrammarParser#var_list.
    def enterVar_list(self, ctx:LangGrammarParser.Var_listContext):
        ctx.type = ctx.parentCtx.type

    # Exit a parse tree produced by LangGrammarParser#var_list.
    def exitVar_list(self, ctx:LangGrammarParser.Var_listContext):
        ctx.code = ''
        if ctx.var_list():
            ctx.code += ctx.var_list().code
        ctx.code += ctx.var().code


    # Enter a parse tree produced by LangGrammarParser#var.
    def enterVar(self, ctx:LangGrammarParser.VarContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#var.
    def exitVar(self, ctx:LangGrammarParser.VarContext):
        try:
            if self.func_name == 'main':
                self.symbol_table.add_identifier(ctx.ID().getText(), self.top, ctx.parentCtx.type)
            else:
                self.symbol_table.add_identifier(ctx.ID().getText(), self.bottom, ctx.parentCtx.type)
        except Exception as e:
            self.printErr(e)

        try:
            identifier = self.symbol_table.find_identifier(ctx.ID().getText())
        except Exception as e:
            self.printErr(e)
        
        ctx.addr = f'm[{identifier.addr}].{self.getIdType(identifier)}'
        
        ctx.type = identifier.type

        if ctx.expr():
            if identifier.type != ctx.expr().type:
                self.printErr(f"Types mismatch on the assignment ({identifier.type}, {ctx.expr().type})")

            ctx.code = ctx.expr().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.expr().addr)};'
        
        else:
            value = 0.0 if ctx.type == 'd' else 0
            ctx.code = f'\n{self.printAddr(ctx.addr)} = {value};'

        if self.func_name == 'main':
            self.top += 1
            ctx.code += '\ntop += 1;'
        else:
            self.bottom += 1
            ctx.code += '\nbottom -= 1;'
            self.used_memory_stack[-1] += 1


    # Enter a parse tree produced by LangGrammarParser#expr.
    def enterExpr(self, ctx:LangGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#expr.
    def exitExpr(self, ctx:LangGrammarParser.ExprContext):
        ctx.addr = ctx.disjnc().addr
            
        ctx.type = ctx.disjnc().type
        
        ctx.code = ctx.disjnc().code


    # Enter a parse tree produced by LangGrammarParser#disjnc.
    def enterDisjnc(self, ctx:LangGrammarParser.DisjncContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#disjnc.
    def exitDisjnc(self, ctx:LangGrammarParser.DisjncContext):
        if ctx.disjnc():
            if ctx.disjnc().type != 'b' or ctx.conjnc().type != 'b':
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")

            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'
            
            ctx.type = 'b'
            
            ctx.code = ctx.disjnc().code + ctx.conjnc().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.disjnc().addr)} && {self.printAddr(ctx.conjnc().addr)};'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.conjnc().addr
            
            ctx.type = ctx.conjnc().type
            
            ctx.code = ctx.conjnc().code


    # Enter a parse tree produced by LangGrammarParser#conjnc.
    def enterConjnc(self, ctx:LangGrammarParser.ConjncContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#conjnc.
    def exitConjnc(self, ctx:LangGrammarParser.ConjncContext):
        if ctx.conjnc():
            if ctx.conjnc().type != 'b' or ctx.xor().type != 'b':
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")

            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'
            
            ctx.type = 'b'
            
            ctx.code = ctx.conjnc().code + ctx.xor().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.conjnc().addr)} && {self.printAddr(ctx.xor().addr)};'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.xor().addr
            
            ctx.type = ctx.xor().type
            
            ctx.code = ctx.xor().code


    # Enter a parse tree produced by LangGrammarParser#xor.
    def enterXor(self, ctx:LangGrammarParser.XorContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#xor.
    def exitXor(self, ctx:LangGrammarParser.XorContext):
        if ctx.xor():
            if ctx.xor().type != 'b' or ctx.comp().type != 'b':
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")

            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'
            
            ctx.type = 'b'
            
            ctx.code = ctx.xor().code + ctx.comp().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.xor().addr)} ^ {self.printAddr(ctx.comp().addr)};'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.comp().addr
            
            ctx.type = ctx.comp().type
            
            ctx.code = ctx.comp().code


    # Enter a parse tree produced by LangGrammarParser#comp.
    def enterComp(self, ctx:LangGrammarParser.CompContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#comp.
    def exitComp(self, ctx:LangGrammarParser.CompContext):
        if len(ctx.children) > 1:
            if ctx.rel(0).type != ctx.rel(1).type:
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")

            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'

            ctx.type = 'b'
            
            ctx.code = ctx.rel(0).code + ctx.rel(1).code
            new_label1 = self.getLabel()
            ctx.code += f'\nif ({self.printAddr(ctx.rel(0).addr)} {ctx.getChild(1)} {self.printAddr(ctx.rel(1).addr)}) goto {new_label1};'
            ctx.code += f'\n{self.printAddr(ctx.addr)} = 0;'
            new_label2 = self.getLabel()
            ctx.code += f'\ngoto {new_label2};'
            ctx.code += f'\n{new_label1}:'
            ctx.code += f'\n{self.printAddr(ctx.addr)} = 1;'
            ctx.code += f'\n{new_label2}:'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.rel(0).addr
            
            ctx.type = ctx.rel(0).type
            
            ctx.code = ctx.rel(0).code


    # Enter a parse tree produced by LangGrammarParser#rel.
    def enterRel(self, ctx:LangGrammarParser.RelContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#rel.
    def exitRel(self, ctx:LangGrammarParser.RelContext):
        if len(ctx.children) > 1:
            if ctx.add(0).type != ctx.add(1).type or \
                (ctx.add(0).type != 'i' and ctx.add(0).type != 'd') or \
                    (ctx.add(1).type != 'i' and ctx.add(1).type != 'd'):
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")

            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'

            ctx.type = 'b'
            
            ctx.code = ctx.add(0).code + ctx.add(1).code
            new_label1 = self.getLabel()
            ctx.code += f'\nif ({self.printAddr(ctx.add(0).addr)} {ctx.getChild(1)} {self.printAddr(ctx.add(1).addr)}) goto {new_label1};'
            ctx.code += f'\n{self.printAddr(ctx.addr)} = 0;'
            new_label2 = self.getLabel()
            ctx.code += f'\ngoto {new_label2};'
            ctx.code += f'\n{new_label1}:'
            ctx.code += f'\n{self.printAddr(ctx.addr)} = 1;'
            ctx.code += f'\n{new_label2}:'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.add(0).addr
            
            ctx.type = ctx.add(0).type
            
            ctx.code = ctx.add(0).code


    # Enter a parse tree produced by LangGrammarParser#add.
    def enterAdd(self, ctx:LangGrammarParser.AddContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#add.
    def exitAdd(self, ctx:LangGrammarParser.AddContext):
        if ctx.add():
            if ctx.add().type != ctx.mul().type or \
                (ctx.add().type != 'i' and ctx.add().type != 'd') or \
                    (ctx.mul().type != 'i' and ctx.mul().type != 'd'):
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")

            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].{self.getIdType(ctx.add())}'
            else:
                ctx.addr = f'm[{self.bottom}].{self.getIdType(ctx.add())}'
            
            ctx.type = ctx.add().type
            
            ctx.code = ctx.add().code + ctx.mul().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.add().addr)} {ctx.getChild(1)} {self.printAddr(ctx.mul().addr)};'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.mul().addr
            
            ctx.type = ctx.mul().type
            
            ctx.code = ctx.mul().code


    # Enter a parse tree produced by LangGrammarParser#mul.
    def enterMul(self, ctx:LangGrammarParser.MulContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#mul.
    def exitMul(self, ctx:LangGrammarParser.MulContext):
        if ctx.mul():
            res_type = ''
            if ctx.getChild(1).getText() == '*':
                if ctx.mul().type == 'i':
                    if ctx.unary().type == 'i':
                        res_type = 'i'
                    elif ctx.unary().typr == 'd':
                        res_type = 'd'
                elif ctx.mul().type == 'd':
                    if ctx.unary().type == 'i' or ctx.unary().type == 'd':
                        res_type = 'd'
            
            elif ctx.getChild(1).getText() == '/':
                if (ctx.mul().type == 'i' or ctx.mul().type == 'd') \
                    and (ctx.unary().type == 'i' or ctx.unary().type == 'd'):
                    res_type = 'd'

            else:
                if (ctx.mul().type == 'i' and ctx.unary().type == 'i'):
                    res_type = 'i'

            if res_type == '':
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")
            
            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].{res_type}'
            else:
                ctx.addr = f'm[{self.bottom}].{res_type}'
            
            ctx.type = res_type
            
            ctx.code = ctx.mul().code + ctx.unary().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {self.printAddr(ctx.mul().addr)} {ctx.getChild(1)} {self.printAddr(ctx.unary().addr)};'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.unary().addr
            
            ctx.type = ctx.unary().type
            
            ctx.code = ctx.unary().code


    # Enter a parse tree produced by LangGrammarParser#unary.
    def enterUnary(self, ctx:LangGrammarParser.UnaryContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#unary.
    def exitUnary(self, ctx:LangGrammarParser.UnaryContext):
        if ctx.unary():
            if (ctx.getChild(0).getText() == '!' and ctx.unary().type != 'b') or \
                not (ctx.getChild(0).getText() == '-' and (ctx.unary().type != 'i' and ctx.unary().type != 'd')):
                self.printErr(f"Operation {ctx.getChild(1).getText()} is not allowed on these types")
                
            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'
            
            ctx.type = 'b'
            
            ctx.code = ctx.unary().code
            ctx.code += f'\n{self.printAddr(ctx.addr)} = {ctx.getChild(0)}{self.printAddr(ctx.unary().addr)};'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1
        
        else:
            ctx.addr = ctx.term().addr
            
            ctx.type = ctx.term().type
            
            ctx.code = ctx.term().code


    # Enter a parse tree produced by LangGrammarParser#term.
    def enterTerm(self, ctx:LangGrammarParser.TermContext):
        if ctx.args():
            ctx.arg_types = []
            ctx.arg_addrs = []

    # Exit a parse tree produced by LangGrammarParser#term.
    def exitTerm(self, ctx:LangGrammarParser.TermContext):
        if ctx.number():
            ctx.addr = ctx.number().addr
            
            ctx.type = ctx.number().type
            
            ctx.code = ''
        
        elif ctx.ID():
            try:
                identifier = self.symbol_table.find_identifier(ctx.ID().getText())
            except Exception as e:
                self.printErr(e)
            
            ctx.type = identifier.type
            
            if ctx.args():
                if not hasattr(identifier, 'args'):
                    self.printErr(f"Variable {ctx.ID().getText()} is not callable")

                a1 = self.flatten_array(ctx.args().arg_types)
                a2 = self.flatten_array(identifier.args)
                if len(a1) != len(a2) or a1 != a2:
                    print(ctx.args().arg_types)
                    print(identifier.args)
                    self.printErr(f"Arguments mismatch for function {ctx.ID().getText()}")

                if ctx.ID().getText() in self.predefined_functions:
                    ctx.code = ctx.args().code

                    if identifier.type != 'v':
                        if self.func_name == 'main':
                            ctx.addr = f'm[{self.top}].{self.getIdType(identifier)}'
                        else:
                            ctx.addr = f'm[{self.bottom}].{self.getIdType(identifier)}'
                        
                        args = ','.join(ctx.args().arg_addrs)
                        ctx.code += f'\n{self.printAddr(ctx.addr)} = {ctx.ID().getText()}({args});'

                        if self.func_name == 'main':
                            self.top += 1
                            ctx.code += '\ntop += 1;'
                        else:
                            self.bottom += 1
                            ctx.code += '\nbottom -= 1;'
                            self.used_memory_stack[-1] += 1
                    
                    else:
                        args = ','.join(ctx.args().arg_addrs)
                        ctx.code += f'\n{ctx.ID().getText()}({args});'

                
                else:
                    new_label = self.getLabel()
                    ctx.code = ctx.args().code
                    ctx.code += f'\nm[top].l = &&{new_label};'
                    ctx.code += f'\ngoto {ctx.ID()};'
                    ctx.code += f'\n{new_label}:'
                
                ctx.addr = f'm[{self.top}].{self.getIdType(identifier)}'
            
            else:
                ctx.addr = f"m[{identifier.addr}].{self.getIdType(identifier)}"

                ctx.code = ''

        elif ctx.BOOL():
            if self.func_name == 'main':
                ctx.addr = f'm[{self.top}].i'
            else:
                ctx.addr = f'm[{self.bottom}].i'
            
            ctx.type = 'b'
            
            if ctx.BOOL().getText() == 'true':
                ctx.code = f'\n{self.printAddr(ctx.addr)} = 1;'
            else:
                ctx.code = f'\n{self.printAddr(ctx.addr)} = 0;'

            if self.func_name == 'main':
                self.top += 1
                ctx.code += '\ntop += 1;'
            else:
                self.bottom += 1
                ctx.code += '\nbottom -= 1;'
                self.used_memory_stack[-1] += 1

        elif ctx.STRING():
            ctx.addr = ctx.STRING().getText()
            
            ctx.type = 's'
            
            ctx.code = ''

        else:
            ctx.addr = ctx.epr().addr
            
            ctx.type = ctx.epr().type
            
            ctx.code = ctx.epr().code


    # Enter a parse tree produced by LangGrammarParser#args.
    def enterArgs(self, ctx:LangGrammarParser.ArgsContext):
        ctx.arg_types = []
        ctx.arg_addrs = []

    # Exit a parse tree produced by LangGrammarParser#args.
    def exitArgs(self, ctx:LangGrammarParser.ArgsContext):
        if ctx.expr():
            ctx.arg_types.append(ctx.expr().type)
            ctx.parentCtx.arg_types.append(ctx.arg_types)

            ctx.arg_addrs.append(self.printAddr(ctx.expr().addr))
            ctx.parentCtx.arg_addrs.append(ctx.arg_addrs)

            ctx.code = ctx.expr().code
            ctx.code += f'\nm[bottom].{self.getIdType(ctx.expr())} = {self.printAddr(ctx.expr().addr)};'
            ctx.code += f'\nbottom -= 1;'
            if ctx.args():
                ctx.code += ctx.args().code
        
        else:
            ctx.code = ''


    # Enter a parse tree produced by LangGrammarParser#number.
    def enterNumber(self, ctx:LangGrammarParser.NumberContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#number.
    def exitNumber(self, ctx:LangGrammarParser.NumberContext):
        ctx.addr = ctx.getText()
        
        if ctx.INT():
            ctx.type = 'i'

        else:
            ctx.type = 'd'
        
        ctx.code = ''


del LangGrammarParser