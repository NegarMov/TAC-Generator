# Generated from LangGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,312,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,3,6,89,8,6,1,7,1,7,3,7,93,8,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,130,8,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,146,
        8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        172,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,182,8,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,192,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,5,13,200,8,13,10,13,12,13,203,9,13,1,14,1,14,1,
        14,1,14,3,14,209,8,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,5,
        16,219,8,16,10,16,12,16,222,9,16,1,17,1,17,1,17,1,17,1,17,1,17,5,
        17,230,8,17,10,17,12,17,233,9,17,1,18,1,18,1,18,1,18,1,18,1,18,5,
        18,241,8,18,10,18,12,18,244,9,18,1,19,1,19,1,19,1,19,1,19,3,19,251,
        8,19,1,20,1,20,1,20,1,20,1,20,3,20,258,8,20,1,21,1,21,1,21,1,21,
        1,21,1,21,5,21,266,8,21,10,21,12,21,269,9,21,1,22,1,22,1,22,1,22,
        1,22,1,22,5,22,277,8,22,10,22,12,22,280,9,22,1,23,1,23,1,23,3,23,
        285,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,300,8,24,1,25,1,25,1,25,1,25,1,25,1,25,3,25,308,8,
        25,1,26,1,26,1,26,0,6,26,32,34,36,42,44,27,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,6,1,0,19,
        20,1,0,21,24,1,0,25,26,1,0,27,29,2,0,26,26,30,30,1,0,34,35,324,0,
        54,1,0,0,0,2,60,1,0,0,0,4,62,1,0,0,0,6,75,1,0,0,0,8,77,1,0,0,0,10,
        80,1,0,0,0,12,88,1,0,0,0,14,92,1,0,0,0,16,129,1,0,0,0,18,145,1,0,
        0,0,20,171,1,0,0,0,22,181,1,0,0,0,24,191,1,0,0,0,26,193,1,0,0,0,
        28,208,1,0,0,0,30,210,1,0,0,0,32,212,1,0,0,0,34,223,1,0,0,0,36,234,
        1,0,0,0,38,250,1,0,0,0,40,257,1,0,0,0,42,259,1,0,0,0,44,270,1,0,
        0,0,46,284,1,0,0,0,48,299,1,0,0,0,50,307,1,0,0,0,52,309,1,0,0,0,
        54,55,3,2,1,0,55,1,1,0,0,0,56,57,3,4,2,0,57,58,3,2,1,0,58,61,1,0,
        0,0,59,61,3,4,2,0,60,56,1,0,0,0,60,59,1,0,0,0,61,3,1,0,0,0,62,63,
        5,31,0,0,63,64,5,33,0,0,64,65,5,1,0,0,65,66,3,6,3,0,66,67,5,2,0,
        0,67,68,3,10,5,0,68,5,1,0,0,0,69,70,3,8,4,0,70,71,5,3,0,0,71,72,
        3,6,3,0,72,76,1,0,0,0,73,76,3,8,4,0,74,76,1,0,0,0,75,69,1,0,0,0,
        75,73,1,0,0,0,75,74,1,0,0,0,76,7,1,0,0,0,77,78,5,31,0,0,78,79,5,
        33,0,0,79,9,1,0,0,0,80,81,5,4,0,0,81,82,3,12,6,0,82,83,5,5,0,0,83,
        11,1,0,0,0,84,85,3,14,7,0,85,86,3,12,6,0,86,89,1,0,0,0,87,89,1,0,
        0,0,88,84,1,0,0,0,88,87,1,0,0,0,89,13,1,0,0,0,90,93,3,16,8,0,91,
        93,3,18,9,0,92,90,1,0,0,0,92,91,1,0,0,0,93,15,1,0,0,0,94,95,5,6,
        0,0,95,96,5,1,0,0,96,97,3,30,15,0,97,98,5,2,0,0,98,99,3,16,8,0,99,
        100,5,7,0,0,100,101,3,16,8,0,101,130,1,0,0,0,102,130,5,8,0,0,103,
        130,3,10,5,0,104,105,5,31,0,0,105,106,3,26,13,0,106,107,5,8,0,0,
        107,130,1,0,0,0,108,109,5,33,0,0,109,110,5,9,0,0,110,111,3,30,15,
        0,111,112,5,8,0,0,112,130,1,0,0,0,113,114,5,33,0,0,114,115,5,10,
        0,0,115,130,5,8,0,0,116,117,5,33,0,0,117,118,5,11,0,0,118,130,5,
        8,0,0,119,120,5,12,0,0,120,130,5,8,0,0,121,122,5,12,0,0,122,123,
        3,30,15,0,123,124,5,8,0,0,124,130,1,0,0,0,125,130,3,20,10,0,126,
        127,3,30,15,0,127,128,5,8,0,0,128,130,1,0,0,0,129,94,1,0,0,0,129,
        102,1,0,0,0,129,103,1,0,0,0,129,104,1,0,0,0,129,108,1,0,0,0,129,
        113,1,0,0,0,129,116,1,0,0,0,129,119,1,0,0,0,129,121,1,0,0,0,129,
        125,1,0,0,0,129,126,1,0,0,0,130,17,1,0,0,0,131,132,5,6,0,0,132,133,
        5,1,0,0,133,134,3,30,15,0,134,135,5,2,0,0,135,136,3,14,7,0,136,146,
        1,0,0,0,137,138,5,6,0,0,138,139,5,1,0,0,139,140,3,30,15,0,140,141,
        5,2,0,0,141,142,3,16,8,0,142,143,5,7,0,0,143,144,3,18,9,0,144,146,
        1,0,0,0,145,131,1,0,0,0,145,137,1,0,0,0,146,19,1,0,0,0,147,148,5,
        13,0,0,148,149,5,1,0,0,149,150,3,30,15,0,150,151,5,2,0,0,151,152,
        3,14,7,0,152,172,1,0,0,0,153,154,5,14,0,0,154,155,3,14,7,0,155,156,
        5,13,0,0,156,157,5,1,0,0,157,158,3,30,15,0,158,159,5,2,0,0,159,160,
        5,8,0,0,160,172,1,0,0,0,161,162,5,15,0,0,162,163,5,1,0,0,163,164,
        3,22,11,0,164,165,5,8,0,0,165,166,3,30,15,0,166,167,5,8,0,0,167,
        168,3,24,12,0,168,169,5,2,0,0,169,170,3,14,7,0,170,172,1,0,0,0,171,
        147,1,0,0,0,171,153,1,0,0,0,171,161,1,0,0,0,172,21,1,0,0,0,173,174,
        5,31,0,0,174,175,5,33,0,0,175,176,5,9,0,0,176,182,3,30,15,0,177,
        178,5,33,0,0,178,179,5,9,0,0,179,182,3,30,15,0,180,182,1,0,0,0,181,
        173,1,0,0,0,181,177,1,0,0,0,181,180,1,0,0,0,182,23,1,0,0,0,183,184,
        5,33,0,0,184,185,5,9,0,0,185,192,3,30,15,0,186,187,5,33,0,0,187,
        192,5,10,0,0,188,189,5,33,0,0,189,192,5,11,0,0,190,192,1,0,0,0,191,
        183,1,0,0,0,191,186,1,0,0,0,191,188,1,0,0,0,191,190,1,0,0,0,192,
        25,1,0,0,0,193,194,6,13,-1,0,194,195,3,28,14,0,195,201,1,0,0,0,196,
        197,10,2,0,0,197,198,5,3,0,0,198,200,3,28,14,0,199,196,1,0,0,0,200,
        203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,27,1,0,0,0,203,201,
        1,0,0,0,204,209,5,33,0,0,205,206,5,33,0,0,206,207,5,9,0,0,207,209,
        3,30,15,0,208,204,1,0,0,0,208,205,1,0,0,0,209,29,1,0,0,0,210,211,
        3,32,16,0,211,31,1,0,0,0,212,213,6,16,-1,0,213,214,3,34,17,0,214,
        220,1,0,0,0,215,216,10,2,0,0,216,217,5,16,0,0,217,219,3,34,17,0,
        218,215,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,
        221,33,1,0,0,0,222,220,1,0,0,0,223,224,6,17,-1,0,224,225,3,36,18,
        0,225,231,1,0,0,0,226,227,10,2,0,0,227,228,5,17,0,0,228,230,3,36,
        18,0,229,226,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,
        0,0,232,35,1,0,0,0,233,231,1,0,0,0,234,235,6,18,-1,0,235,236,3,38,
        19,0,236,242,1,0,0,0,237,238,10,2,0,0,238,239,5,18,0,0,239,241,3,
        38,19,0,240,237,1,0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,
        1,0,0,0,243,37,1,0,0,0,244,242,1,0,0,0,245,246,3,40,20,0,246,247,
        7,0,0,0,247,248,3,40,20,0,248,251,1,0,0,0,249,251,3,40,20,0,250,
        245,1,0,0,0,250,249,1,0,0,0,251,39,1,0,0,0,252,253,3,42,21,0,253,
        254,7,1,0,0,254,255,3,42,21,0,255,258,1,0,0,0,256,258,3,42,21,0,
        257,252,1,0,0,0,257,256,1,0,0,0,258,41,1,0,0,0,259,260,6,21,-1,0,
        260,261,3,44,22,0,261,267,1,0,0,0,262,263,10,2,0,0,263,264,7,2,0,
        0,264,266,3,44,22,0,265,262,1,0,0,0,266,269,1,0,0,0,267,265,1,0,
        0,0,267,268,1,0,0,0,268,43,1,0,0,0,269,267,1,0,0,0,270,271,6,22,
        -1,0,271,272,3,46,23,0,272,278,1,0,0,0,273,274,10,2,0,0,274,275,
        7,3,0,0,275,277,3,46,23,0,276,273,1,0,0,0,277,280,1,0,0,0,278,276,
        1,0,0,0,278,279,1,0,0,0,279,45,1,0,0,0,280,278,1,0,0,0,281,282,7,
        4,0,0,282,285,3,46,23,0,283,285,3,48,24,0,284,281,1,0,0,0,284,283,
        1,0,0,0,285,47,1,0,0,0,286,300,3,52,26,0,287,300,5,33,0,0,288,300,
        5,32,0,0,289,300,5,36,0,0,290,291,5,33,0,0,291,292,5,1,0,0,292,293,
        3,50,25,0,293,294,5,2,0,0,294,300,1,0,0,0,295,296,5,1,0,0,296,297,
        3,30,15,0,297,298,5,2,0,0,298,300,1,0,0,0,299,286,1,0,0,0,299,287,
        1,0,0,0,299,288,1,0,0,0,299,289,1,0,0,0,299,290,1,0,0,0,299,295,
        1,0,0,0,300,49,1,0,0,0,301,302,3,30,15,0,302,303,5,3,0,0,303,304,
        3,50,25,0,304,308,1,0,0,0,305,308,3,30,15,0,306,308,1,0,0,0,307,
        301,1,0,0,0,307,305,1,0,0,0,307,306,1,0,0,0,308,51,1,0,0,0,309,310,
        7,5,0,0,310,53,1,0,0,0,21,60,75,88,92,129,145,171,181,191,201,208,
        220,231,242,250,257,267,278,284,299,307
    ]

class LangGrammarParser ( Parser ):

    grammarFileName = "LangGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'{'", "'}'", "'if'", 
                     "'else'", "';'", "'='", "'++'", "'--'", "'return'", 
                     "'while'", "'do'", "'for'", "'||'", "'&&'", "'^'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DATA_TYPE", 
                      "BOOL", "ID", "DOUBLE", "INT", "STRING", "WS", "MULTI_COMMENT", 
                      "SINGLE_COMMENT" ]

    RULE_prog = 0
    RULE_func_list = 1
    RULE_func_def = 2
    RULE_param_list = 3
    RULE_param = 4
    RULE_code_block = 5
    RULE_stmt_list = 6
    RULE_stmt = 7
    RULE_decide_with_else = 8
    RULE_decide_no_else = 9
    RULE_loop_stmt = 10
    RULE_init_stmt = 11
    RULE_post_stmt = 12
    RULE_var_list = 13
    RULE_var = 14
    RULE_expr = 15
    RULE_disjnc = 16
    RULE_conjnc = 17
    RULE_xor = 18
    RULE_comp = 19
    RULE_rel = 20
    RULE_add = 21
    RULE_mul = 22
    RULE_unary = 23
    RULE_term = 24
    RULE_args = 25
    RULE_number = 26

    ruleNames =  [ "prog", "func_list", "func_def", "param_list", "param", 
                   "code_block", "stmt_list", "stmt", "decide_with_else", 
                   "decide_no_else", "loop_stmt", "init_stmt", "post_stmt", 
                   "var_list", "var", "expr", "disjnc", "conjnc", "xor", 
                   "comp", "rel", "add", "mul", "unary", "term", "args", 
                   "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    DATA_TYPE=31
    BOOL=32
    ID=33
    DOUBLE=34
    INT=35
    STRING=36
    WS=37
    MULTI_COMMENT=38
    SINGLE_COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Func_listContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = LangGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.func_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_def(self):
            return self.getTypedRuleContext(LangGrammarParser.Func_defContext,0)


        def func_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Func_listContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_func_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_list" ):
                listener.enterFunc_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_list" ):
                listener.exitFunc_list(self)




    def func_list(self):

        localctx = LangGrammarParser.Func_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func_list)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.func_def()
                self.state = 57
                self.func_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.func_def()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(LangGrammarParser.DATA_TYPE, 0)

        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def param_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Param_listContext,0)


        def code_block(self):
            return self.getTypedRuleContext(LangGrammarParser.Code_blockContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)




    def func_def(self):

        localctx = LangGrammarParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(LangGrammarParser.DATA_TYPE)
            self.state = 63
            self.match(LangGrammarParser.ID)
            self.state = 64
            self.match(LangGrammarParser.T__0)
            self.state = 65
            self.param_list()
            self.state = 66
            self.match(LangGrammarParser.T__1)
            self.state = 67
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(LangGrammarParser.ParamContext,0)


        def param_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Param_listContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = LangGrammarParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param_list)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.param()
                self.state = 70
                self.match(LangGrammarParser.T__2)
                self.state = 71
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.param()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(LangGrammarParser.DATA_TYPE, 0)

        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = LangGrammarParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(LangGrammarParser.DATA_TYPE)
            self.state = 78
            self.match(LangGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = LangGrammarParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LangGrammarParser.T__3)
            self.state = 81
            self.stmt_list()
            self.state = 82
            self.match(LangGrammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(LangGrammarParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_stmt_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)




    def stmt_list(self):

        localctx = LangGrammarParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt_list)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 4, 6, 8, 12, 13, 14, 15, 26, 30, 31, 32, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.stmt()
                self.state = 85
                self.stmt_list()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decide_with_else(self):
            return self.getTypedRuleContext(LangGrammarParser.Decide_with_elseContext,0)


        def decide_no_else(self):
            return self.getTypedRuleContext(LangGrammarParser.Decide_no_elseContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = LangGrammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.decide_with_else()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.decide_no_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decide_with_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def decide_with_else(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.Decide_with_elseContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.Decide_with_elseContext,i)


        def code_block(self):
            return self.getTypedRuleContext(LangGrammarParser.Code_blockContext,0)


        def DATA_TYPE(self):
            return self.getToken(LangGrammarParser.DATA_TYPE, 0)

        def var_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Var_listContext,0)


        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def loop_stmt(self):
            return self.getTypedRuleContext(LangGrammarParser.Loop_stmtContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_decide_with_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecide_with_else" ):
                listener.enterDecide_with_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecide_with_else" ):
                listener.exitDecide_with_else(self)




    def decide_with_else(self):

        localctx = LangGrammarParser.Decide_with_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decide_with_else)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(LangGrammarParser.T__5)
                self.state = 95
                self.match(LangGrammarParser.T__0)
                self.state = 96
                self.expr()
                self.state = 97
                self.match(LangGrammarParser.T__1)
                self.state = 98
                self.decide_with_else()
                self.state = 99
                self.match(LangGrammarParser.T__6)
                self.state = 100
                self.decide_with_else()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.code_block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(LangGrammarParser.DATA_TYPE)
                self.state = 105
                self.var_list(0)
                self.state = 106
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.match(LangGrammarParser.ID)
                self.state = 109
                self.match(LangGrammarParser.T__8)
                self.state = 110
                self.expr()
                self.state = 111
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.match(LangGrammarParser.ID)
                self.state = 114
                self.match(LangGrammarParser.T__9)
                self.state = 115
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.match(LangGrammarParser.ID)
                self.state = 117
                self.match(LangGrammarParser.T__10)
                self.state = 118
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 119
                self.match(LangGrammarParser.T__11)
                self.state = 120
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 121
                self.match(LangGrammarParser.T__11)
                self.state = 122
                self.expr()
                self.state = 123
                self.match(LangGrammarParser.T__7)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 125
                self.loop_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 126
                self.expr()
                self.state = 127
                self.match(LangGrammarParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decide_no_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(LangGrammarParser.StmtContext,0)


        def decide_with_else(self):
            return self.getTypedRuleContext(LangGrammarParser.Decide_with_elseContext,0)


        def decide_no_else(self):
            return self.getTypedRuleContext(LangGrammarParser.Decide_no_elseContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_decide_no_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecide_no_else" ):
                listener.enterDecide_no_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecide_no_else" ):
                listener.exitDecide_no_else(self)




    def decide_no_else(self):

        localctx = LangGrammarParser.Decide_no_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decide_no_else)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(LangGrammarParser.T__5)
                self.state = 132
                self.match(LangGrammarParser.T__0)
                self.state = 133
                self.expr()
                self.state = 134
                self.match(LangGrammarParser.T__1)
                self.state = 135
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(LangGrammarParser.T__5)
                self.state = 138
                self.match(LangGrammarParser.T__0)
                self.state = 139
                self.expr()
                self.state = 140
                self.match(LangGrammarParser.T__1)
                self.state = 141
                self.decide_with_else()
                self.state = 142
                self.match(LangGrammarParser.T__6)
                self.state = 143
                self.decide_no_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(LangGrammarParser.StmtContext,0)


        def init_stmt(self):
            return self.getTypedRuleContext(LangGrammarParser.Init_stmtContext,0)


        def post_stmt(self):
            return self.getTypedRuleContext(LangGrammarParser.Post_stmtContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_loop_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_stmt" ):
                listener.enterLoop_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_stmt" ):
                listener.exitLoop_stmt(self)




    def loop_stmt(self):

        localctx = LangGrammarParser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_loop_stmt)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(LangGrammarParser.T__12)
                self.state = 148
                self.match(LangGrammarParser.T__0)
                self.state = 149
                self.expr()
                self.state = 150
                self.match(LangGrammarParser.T__1)
                self.state = 151
                self.stmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(LangGrammarParser.T__13)
                self.state = 154
                self.stmt()
                self.state = 155
                self.match(LangGrammarParser.T__12)
                self.state = 156
                self.match(LangGrammarParser.T__0)
                self.state = 157
                self.expr()
                self.state = 158
                self.match(LangGrammarParser.T__1)
                self.state = 159
                self.match(LangGrammarParser.T__7)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.match(LangGrammarParser.T__14)
                self.state = 162
                self.match(LangGrammarParser.T__0)
                self.state = 163
                self.init_stmt()
                self.state = 164
                self.match(LangGrammarParser.T__7)
                self.state = 165
                self.expr()
                self.state = 166
                self.match(LangGrammarParser.T__7)
                self.state = 167
                self.post_stmt()
                self.state = 168
                self.match(LangGrammarParser.T__1)
                self.state = 169
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_TYPE(self):
            return self.getToken(LangGrammarParser.DATA_TYPE, 0)

        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_init_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit_stmt" ):
                listener.enterInit_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit_stmt" ):
                listener.exitInit_stmt(self)




    def init_stmt(self):

        localctx = LangGrammarParser.Init_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_init_stmt)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(LangGrammarParser.DATA_TYPE)
                self.state = 174
                self.match(LangGrammarParser.ID)
                self.state = 175
                self.match(LangGrammarParser.T__8)
                self.state = 176
                self.expr()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(LangGrammarParser.ID)
                self.state = 178
                self.match(LangGrammarParser.T__8)
                self.state = 179
                self.expr()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Post_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_post_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPost_stmt" ):
                listener.enterPost_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPost_stmt" ):
                listener.exitPost_stmt(self)




    def post_stmt(self):

        localctx = LangGrammarParser.Post_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_post_stmt)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(LangGrammarParser.ID)
                self.state = 184
                self.match(LangGrammarParser.T__8)
                self.state = 185
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(LangGrammarParser.ID)
                self.state = 187
                self.match(LangGrammarParser.T__9)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(LangGrammarParser.ID)
                self.state = 189
                self.match(LangGrammarParser.T__10)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LangGrammarParser.VarContext,0)


        def var_list(self):
            return self.getTypedRuleContext(LangGrammarParser.Var_listContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_var_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_list" ):
                listener.enterVar_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_list" ):
                listener.exitVar_list(self)



    def var_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangGrammarParser.Var_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_var_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.var()
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LangGrammarParser.Var_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_list)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    self.match(LangGrammarParser.T__2)
                    self.state = 198
                    self.var() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = LangGrammarParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(LangGrammarParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(LangGrammarParser.ID)
                self.state = 206
                self.match(LangGrammarParser.T__8)
                self.state = 207
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjnc(self):
            return self.getTypedRuleContext(LangGrammarParser.DisjncContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = LangGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.disjnc(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisjncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjnc(self):
            return self.getTypedRuleContext(LangGrammarParser.ConjncContext,0)


        def disjnc(self):
            return self.getTypedRuleContext(LangGrammarParser.DisjncContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_disjnc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjnc" ):
                listener.enterDisjnc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjnc" ):
                listener.exitDisjnc(self)



    def disjnc(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangGrammarParser.DisjncContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_disjnc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.conjnc(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LangGrammarParser.DisjncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_disjnc)
                    self.state = 215
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 216
                    self.match(LangGrammarParser.T__15)
                    self.state = 217
                    self.conjnc(0) 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConjncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xor(self):
            return self.getTypedRuleContext(LangGrammarParser.XorContext,0)


        def conjnc(self):
            return self.getTypedRuleContext(LangGrammarParser.ConjncContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_conjnc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjnc" ):
                listener.enterConjnc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjnc" ):
                listener.exitConjnc(self)



    def conjnc(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangGrammarParser.ConjncContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_conjnc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.xor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LangGrammarParser.ConjncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conjnc)
                    self.state = 226
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 227
                    self.match(LangGrammarParser.T__16)
                    self.state = 228
                    self.xor(0) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class XorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(LangGrammarParser.CompContext,0)


        def xor(self):
            return self.getTypedRuleContext(LangGrammarParser.XorContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_xor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXor" ):
                listener.enterXor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXor" ):
                listener.exitXor(self)



    def xor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangGrammarParser.XorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_xor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.comp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LangGrammarParser.XorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_xor)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    self.match(LangGrammarParser.T__17)
                    self.state = 239
                    self.comp() 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.RelContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.RelContext,i)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = LangGrammarParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.rel()
                self.state = 246
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.rel()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.rel()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.AddContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.AddContext,i)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel" ):
                listener.enterRel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel" ):
                listener.exitRel(self)




    def rel(self):

        localctx = LangGrammarParser.RelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_rel)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.add(0)
                self.state = 253
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 254
                self.add(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.add(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul(self):
            return self.getTypedRuleContext(LangGrammarParser.MulContext,0)


        def add(self):
            return self.getTypedRuleContext(LangGrammarParser.AddContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)



    def add(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangGrammarParser.AddContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_add, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.mul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LangGrammarParser.AddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add)
                    self.state = 262
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 263
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 264
                    self.mul(0) 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(LangGrammarParser.UnaryContext,0)


        def mul(self):
            return self.getTypedRuleContext(LangGrammarParser.MulContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)



    def mul(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangGrammarParser.MulContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_mul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LangGrammarParser.MulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 275
                    self.unary() 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(LangGrammarParser.UnaryContext,0)


        def term(self):
            return self.getTypedRuleContext(LangGrammarParser.TermContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = LangGrammarParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                _la = self._input.LA(1)
                if not(_la==26 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 282
                self.unary()
                pass
            elif token in [1, 32, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.term()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(LangGrammarParser.NumberContext,0)


        def ID(self):
            return self.getToken(LangGrammarParser.ID, 0)

        def BOOL(self):
            return self.getToken(LangGrammarParser.BOOL, 0)

        def STRING(self):
            return self.getToken(LangGrammarParser.STRING, 0)

        def args(self):
            return self.getTypedRuleContext(LangGrammarParser.ArgsContext,0)


        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = LangGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(LangGrammarParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.match(LangGrammarParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 289
                self.match(LangGrammarParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 290
                self.match(LangGrammarParser.ID)
                self.state = 291
                self.match(LangGrammarParser.T__0)
                self.state = 292
                self.args()
                self.state = 293
                self.match(LangGrammarParser.T__1)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 295
                self.match(LangGrammarParser.T__0)
                self.state = 296
                self.expr()
                self.state = 297
                self.match(LangGrammarParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LangGrammarParser.ExprContext,0)


        def args(self):
            return self.getTypedRuleContext(LangGrammarParser.ArgsContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = LangGrammarParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_args)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.expr()
                self.state = 302
                self.match(LangGrammarParser.T__2)
                self.state = 303
                self.args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LangGrammarParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(LangGrammarParser.DOUBLE, 0)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = LangGrammarParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not(_la==34 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.var_list_sempred
        self._predicates[16] = self.disjnc_sempred
        self._predicates[17] = self.conjnc_sempred
        self._predicates[18] = self.xor_sempred
        self._predicates[21] = self.add_sempred
        self._predicates[22] = self.mul_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def var_list_sempred(self, localctx:Var_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def disjnc_sempred(self, localctx:DisjncContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def conjnc_sempred(self, localctx:ConjncContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def xor_sempred(self, localctx:XorContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def add_sempred(self, localctx:AddContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def mul_sempred(self, localctx:MulContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




