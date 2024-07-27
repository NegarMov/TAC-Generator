grammar LangGrammar;

prog
	: func_list ;


func_list
	: func_def func_list
	| func_def
	;

func_def
	: DATA_TYPE ID '(' param_list ')' code_block ;

param_list
	: param ',' param_list
	| param
	|
	;

param
	: DATA_TYPE ID ;

code_block
	: '{' stmt_list '}' ;

stmt_list
	: stmt stmt_list 
	|
	;

stmt
	: decide_with_else
	| decide_no_else
	;

decide_with_else
	: 'if' '(' expr ')' decide_with_else 'else' decide_with_else
	| ';' 
	| code_block
	| DATA_TYPE var_list ';'
	| ID '=' expr ';'
	| ID '++' ';'
	| ID '--' ';'
	| 'return' ';'
	| 'return' expr ';'
	| loop_stmt
	| expr ';'
	;

decide_no_else
	: 'if' '(' expr ')' stmt
	| 'if' '(' expr ')' decide_with_else 'else' decide_no_else
	;

loop_stmt
	: 'while' '(' expr ')' stmt
	| 'do' stmt 'while' '(' expr ')' ';'
	| 'for' '(' init_stmt ';' expr ';' post_stmt ')' stmt
	;

init_stmt
	: DATA_TYPE ID '=' expr
	| ID '=' expr
	|
	;

post_stmt
	: ID '=' expr
	| ID '++'
	| ID '--'
	|
	;

var_list
	: var_list ',' var
	| var
	;

var
	: ID
	| ID '=' expr
	;

expr
	: disjnc ;

disjnc
	: disjnc '||' conjnc
	| conjnc
	;

conjnc
	: conjnc '&&' xor
	| xor
	;

xor
	: xor '^' comp
	| comp
	;

comp
	: rel ('==' | '!=') rel
	| rel
	;

rel
	: add ('<' | '>' | '<=' | '>=') add
	| add
	;


add
	: add ('+' | '-') mul
	| mul
	;

mul
	: mul ('*' | '/' | '%') unary
	| unary
	;

unary
	: ('-' | '!') unary
	| term
	;

term
	: number
	| ID	
	| BOOL	
	| STRING
	| ID '(' args ')'
	| '(' expr ')'
	;

args
	: expr ',' args
	| expr
	|
	;

number
	: INT
	| DOUBLE
	;

DATA_TYPE	
	: 'int' 
	| 'double'
	| 'boolean'
	| 'void'
	;

BOOL
	: 'true'
	| 'false'
	;

ID
	: [_a-zA-Z][_a-zA-Z0-9]* ;

DOUBLE	
	: INT '.' [0-9]* ('e' ('+'|'-')? INT)? ;

INT
	: '0'
	| [1-9][0-9]* ;

STRING
    : '"' (~["\\\n] | ('\\' [\\"'tbr]))* '"' ;

WS
	: [ \t\r\n]+ -> skip ;

MULTI_COMMENT
    : '/*' .*? '*/' -> skip ;

SINGLE_COMMENT
    : '//' ~[\r\n]* -> skip ;