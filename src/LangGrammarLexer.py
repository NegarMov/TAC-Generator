# Generated from LangGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,39,271,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,
        0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,18,
        1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,23,
        1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,184,8,30,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,195,8,31,1,32,1,32,5,32,
        199,8,32,10,32,12,32,202,9,32,1,33,1,33,1,33,5,33,207,8,33,10,33,
        12,33,210,9,33,1,33,1,33,3,33,214,8,33,1,33,3,33,217,8,33,1,34,1,
        34,1,34,5,34,222,8,34,10,34,12,34,225,9,34,3,34,227,8,34,1,35,1,
        35,1,35,1,35,5,35,233,8,35,10,35,12,35,236,9,35,1,35,1,35,1,36,4,
        36,241,8,36,11,36,12,36,242,1,36,1,36,1,37,1,37,1,37,1,37,5,37,251,
        8,37,10,37,12,37,254,9,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,5,38,265,8,38,10,38,12,38,268,9,38,1,38,1,38,1,252,0,39,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,
        73,37,75,38,77,39,1,0,9,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,
        95,97,122,1,0,48,57,2,0,43,43,45,45,1,0,49,57,3,0,10,10,34,34,92,
        92,6,0,34,34,39,39,92,92,98,98,114,114,116,116,3,0,9,10,13,13,32,
        32,2,0,10,10,13,13,285,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,1,79,1,0,0,0,3,81,1,0,0,0,5,83,1,0,0,0,7,85,1,0,0,0,9,87,1,
        0,0,0,11,89,1,0,0,0,13,92,1,0,0,0,15,97,1,0,0,0,17,99,1,0,0,0,19,
        101,1,0,0,0,21,104,1,0,0,0,23,107,1,0,0,0,25,114,1,0,0,0,27,120,
        1,0,0,0,29,123,1,0,0,0,31,127,1,0,0,0,33,130,1,0,0,0,35,133,1,0,
        0,0,37,135,1,0,0,0,39,138,1,0,0,0,41,141,1,0,0,0,43,143,1,0,0,0,
        45,145,1,0,0,0,47,148,1,0,0,0,49,151,1,0,0,0,51,153,1,0,0,0,53,155,
        1,0,0,0,55,157,1,0,0,0,57,159,1,0,0,0,59,161,1,0,0,0,61,183,1,0,
        0,0,63,194,1,0,0,0,65,196,1,0,0,0,67,203,1,0,0,0,69,226,1,0,0,0,
        71,228,1,0,0,0,73,240,1,0,0,0,75,246,1,0,0,0,77,260,1,0,0,0,79,80,
        5,40,0,0,80,2,1,0,0,0,81,82,5,41,0,0,82,4,1,0,0,0,83,84,5,44,0,0,
        84,6,1,0,0,0,85,86,5,123,0,0,86,8,1,0,0,0,87,88,5,125,0,0,88,10,
        1,0,0,0,89,90,5,105,0,0,90,91,5,102,0,0,91,12,1,0,0,0,92,93,5,101,
        0,0,93,94,5,108,0,0,94,95,5,115,0,0,95,96,5,101,0,0,96,14,1,0,0,
        0,97,98,5,59,0,0,98,16,1,0,0,0,99,100,5,61,0,0,100,18,1,0,0,0,101,
        102,5,43,0,0,102,103,5,43,0,0,103,20,1,0,0,0,104,105,5,45,0,0,105,
        106,5,45,0,0,106,22,1,0,0,0,107,108,5,114,0,0,108,109,5,101,0,0,
        109,110,5,116,0,0,110,111,5,117,0,0,111,112,5,114,0,0,112,113,5,
        110,0,0,113,24,1,0,0,0,114,115,5,119,0,0,115,116,5,104,0,0,116,117,
        5,105,0,0,117,118,5,108,0,0,118,119,5,101,0,0,119,26,1,0,0,0,120,
        121,5,100,0,0,121,122,5,111,0,0,122,28,1,0,0,0,123,124,5,102,0,0,
        124,125,5,111,0,0,125,126,5,114,0,0,126,30,1,0,0,0,127,128,5,124,
        0,0,128,129,5,124,0,0,129,32,1,0,0,0,130,131,5,38,0,0,131,132,5,
        38,0,0,132,34,1,0,0,0,133,134,5,94,0,0,134,36,1,0,0,0,135,136,5,
        61,0,0,136,137,5,61,0,0,137,38,1,0,0,0,138,139,5,33,0,0,139,140,
        5,61,0,0,140,40,1,0,0,0,141,142,5,60,0,0,142,42,1,0,0,0,143,144,
        5,62,0,0,144,44,1,0,0,0,145,146,5,60,0,0,146,147,5,61,0,0,147,46,
        1,0,0,0,148,149,5,62,0,0,149,150,5,61,0,0,150,48,1,0,0,0,151,152,
        5,43,0,0,152,50,1,0,0,0,153,154,5,45,0,0,154,52,1,0,0,0,155,156,
        5,42,0,0,156,54,1,0,0,0,157,158,5,47,0,0,158,56,1,0,0,0,159,160,
        5,37,0,0,160,58,1,0,0,0,161,162,5,33,0,0,162,60,1,0,0,0,163,164,
        5,105,0,0,164,165,5,110,0,0,165,184,5,116,0,0,166,167,5,100,0,0,
        167,168,5,111,0,0,168,169,5,117,0,0,169,170,5,98,0,0,170,171,5,108,
        0,0,171,184,5,101,0,0,172,173,5,98,0,0,173,174,5,111,0,0,174,175,
        5,111,0,0,175,176,5,108,0,0,176,177,5,101,0,0,177,178,5,97,0,0,178,
        184,5,110,0,0,179,180,5,118,0,0,180,181,5,111,0,0,181,182,5,105,
        0,0,182,184,5,100,0,0,183,163,1,0,0,0,183,166,1,0,0,0,183,172,1,
        0,0,0,183,179,1,0,0,0,184,62,1,0,0,0,185,186,5,116,0,0,186,187,5,
        114,0,0,187,188,5,117,0,0,188,195,5,101,0,0,189,190,5,102,0,0,190,
        191,5,97,0,0,191,192,5,108,0,0,192,193,5,115,0,0,193,195,5,101,0,
        0,194,185,1,0,0,0,194,189,1,0,0,0,195,64,1,0,0,0,196,200,7,0,0,0,
        197,199,7,1,0,0,198,197,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,
        200,201,1,0,0,0,201,66,1,0,0,0,202,200,1,0,0,0,203,204,3,69,34,0,
        204,208,5,46,0,0,205,207,7,2,0,0,206,205,1,0,0,0,207,210,1,0,0,0,
        208,206,1,0,0,0,208,209,1,0,0,0,209,216,1,0,0,0,210,208,1,0,0,0,
        211,213,5,101,0,0,212,214,7,3,0,0,213,212,1,0,0,0,213,214,1,0,0,
        0,214,215,1,0,0,0,215,217,3,69,34,0,216,211,1,0,0,0,216,217,1,0,
        0,0,217,68,1,0,0,0,218,227,5,48,0,0,219,223,7,4,0,0,220,222,7,2,
        0,0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,
        0,0,224,227,1,0,0,0,225,223,1,0,0,0,226,218,1,0,0,0,226,219,1,0,
        0,0,227,70,1,0,0,0,228,234,5,34,0,0,229,233,8,5,0,0,230,231,5,92,
        0,0,231,233,7,6,0,0,232,229,1,0,0,0,232,230,1,0,0,0,233,236,1,0,
        0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,234,1,0,
        0,0,237,238,5,34,0,0,238,72,1,0,0,0,239,241,7,7,0,0,240,239,1,0,
        0,0,241,242,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,244,1,0,
        0,0,244,245,6,36,0,0,245,74,1,0,0,0,246,247,5,47,0,0,247,248,5,42,
        0,0,248,252,1,0,0,0,249,251,9,0,0,0,250,249,1,0,0,0,251,254,1,0,
        0,0,252,253,1,0,0,0,252,250,1,0,0,0,253,255,1,0,0,0,254,252,1,0,
        0,0,255,256,5,42,0,0,256,257,5,47,0,0,257,258,1,0,0,0,258,259,6,
        37,0,0,259,76,1,0,0,0,260,261,5,47,0,0,261,262,5,47,0,0,262,266,
        1,0,0,0,263,265,8,8,0,0,264,263,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,266,267,1,0,0,0,267,269,1,0,0,0,268,266,1,0,0,0,269,270,
        6,38,0,0,270,78,1,0,0,0,14,0,183,194,200,208,213,216,223,226,232,
        234,242,252,266,1,6,0,0
    ]

class LangGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    DATA_TYPE = 31
    BOOL = 32
    ID = 33
    DOUBLE = 34
    INT = 35
    STRING = 36
    WS = 37
    MULTI_COMMENT = 38
    SINGLE_COMMENT = 39

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'{'", "'}'", "'if'", "'else'", "';'", 
            "'='", "'++'", "'--'", "'return'", "'while'", "'do'", "'for'", 
            "'||'", "'&&'", "'^'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "DATA_TYPE", "BOOL", "ID", "DOUBLE", "INT", "STRING", "WS", 
            "MULTI_COMMENT", "SINGLE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "DATA_TYPE", "BOOL", 
                  "ID", "DOUBLE", "INT", "STRING", "WS", "MULTI_COMMENT", 
                  "SINGLE_COMMENT" ]

    grammarFileName = "LangGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


