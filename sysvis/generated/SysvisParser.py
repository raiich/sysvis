# Generated from Sysvis.g4 by ANTLR 4.7.1
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\5\2$\n\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\7\4-\n\4\f\4\16\4\60\13\4\3\4\5\4\63")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5<\n\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tT\n\t\3\n\3\n\5\nX\n\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\rk\n\r\3\r\2\2\16\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\2\3\3\2\f\17\2n\2\32\3\2\2\2\4\'\3\2\2")
        buf.write("\2\6)\3\2\2\2\b;\3\2\2\2\n=\3\2\2\2\f@\3\2\2\2\16K\3\2")
        buf.write("\2\2\20O\3\2\2\2\22U\3\2\2\2\24Y\3\2\2\2\26_\3\2\2\2\30")
        buf.write("e\3\2\2\2\32\37\5\4\3\2\33\34\7\3\2\2\34\36\5\4\3\2\35")
        buf.write("\33\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 #\3")
        buf.write("\2\2\2!\37\3\2\2\2\"$\7\3\2\2#\"\3\2\2\2#$\3\2\2\2$%\3")
        buf.write("\2\2\2%&\7\2\2\3&\3\3\2\2\2\'(\5\6\4\2(\5\3\2\2\2).\5")
        buf.write("\b\5\2*+\7\4\2\2+-\5\b\5\2,*\3\2\2\2-\60\3\2\2\2.,\3\2")
        buf.write("\2\2./\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\61\63\7\4\2\2\62")
        buf.write("\61\3\2\2\2\62\63\3\2\2\2\63\7\3\2\2\2\64<\5\22\n\2\65")
        buf.write("<\5\20\t\2\66<\5\n\6\2\67<\5\16\b\28<\5\24\13\29<\5\26")
        buf.write("\f\2:<\5\30\r\2;\64\3\2\2\2;\65\3\2\2\2;\66\3\2\2\2;\67")
        buf.write("\3\2\2\2;8\3\2\2\2;9\3\2\2\2;:\3\2\2\2<\t\3\2\2\2=>\t")
        buf.write("\2\2\2>?\5\f\7\2?\13\3\2\2\2@A\7\5\2\2AF\5\16\b\2BC\7")
        buf.write("\6\2\2CE\5\16\b\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2")
        buf.write("\2\2GI\3\2\2\2HF\3\2\2\2IJ\7\7\2\2J\r\3\2\2\2KL\7\21\2")
        buf.write("\2LM\7\b\2\2MN\7\21\2\2N\17\3\2\2\2OP\7\21\2\2PQ\7\t\2")
        buf.write("\2QS\7\21\2\2RT\5\f\7\2SR\3\2\2\2ST\3\2\2\2T\21\3\2\2")
        buf.write("\2UW\7\21\2\2VX\5\f\7\2WV\3\2\2\2WX\3\2\2\2X\23\3\2\2")
        buf.write("\2YZ\7\16\2\2Z[\7\21\2\2[\\\7\n\2\2\\]\5\6\4\2]^\7\13")
        buf.write("\2\2^\25\3\2\2\2_`\7\17\2\2`a\7\21\2\2ab\7\n\2\2bc\5\6")
        buf.write("\4\2cd\7\13\2\2d\27\3\2\2\2ej\7\20\2\2fk\7\21\2\2gh\7")
        buf.write("\21\2\2hi\7\t\2\2ik\7\21\2\2jf\3\2\2\2jg\3\2\2\2k\31\3")
        buf.write("\2\2\2\13\37#.\62;FSWj")
        return buf.getvalue()


class SysvisParser(Parser):
    grammarFileName = "Sysvis.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'---'", "';'", "'['", "','", "']'", "'='",
                    "'->'", "'{'", "'}'", "'node'", "'edge'", "'group'",
                    "'zone'", "'delete'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "NODE", "EDGE", "GROUP",
                     "ZONE", "DELETE", "ID", "SPACES"]

    RULE_story = 0
    RULE_moment = 1
    RULE_stmt_list = 2
    RULE_stmt = 3
    RULE_attr_stmt = 4
    RULE_attr_list = 5
    RULE_assignment = 6
    RULE_edge_stmt = 7
    RULE_node_stmt = 8
    RULE_group = 9
    RULE_zone = 10
    RULE_delete = 11

    ruleNames = ["story", "moment", "stmt_list", "stmt", "attr_stmt",
                 "attr_list", "assignment", "edge_stmt", "node_stmt",
                 "group", "zone", "delete"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    NODE = 10
    EDGE = 11
    GROUP = 12
    ZONE = 13
    DELETE = 14
    ID = 15
    SPACES = 16

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class StoryContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moment(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SysvisParser.MomentContext)
            else:
                return self.getTypedRuleContext(SysvisParser.MomentContext, i)

        def EOF(self):
            return self.getToken(SysvisParser.EOF, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_story

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStory"):
                return visitor.visitStory(self)
            else:
                return visitor.visitChildren(self)

    def story(self):

        localctx = SysvisParser.StoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_story)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.moment()
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 0, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 25
                    self.match(SysvisParser.T__0)
                    self.state = 26
                    self.moment()
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 0, self._ctx)

            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SysvisParser.T__0:
                self.state = 32
                self.match(SysvisParser.T__0)

            self.state = 35
            self.match(SysvisParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MomentContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(SysvisParser.Stmt_listContext, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_moment

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMoment"):
                return visitor.visitMoment(self)
            else:
                return visitor.visitChildren(self)

    def moment(self):

        localctx = SysvisParser.MomentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_moment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SysvisParser.StmtContext)
            else:
                return self.getTypedRuleContext(SysvisParser.StmtContext, i)

        def getRuleIndex(self):
            return SysvisParser.RULE_stmt_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt_list"):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)

    def stmt_list(self):

        localctx = SysvisParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt_list)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.stmt()
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 40
                    self.match(SysvisParser.T__1)
                    self.state = 41
                    self.stmt()
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SysvisParser.T__1:
                self.state = 47
                self.match(SysvisParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node_stmt(self):
            return self.getTypedRuleContext(SysvisParser.Node_stmtContext, 0)

        def edge_stmt(self):
            return self.getTypedRuleContext(SysvisParser.Edge_stmtContext, 0)

        def attr_stmt(self):
            return self.getTypedRuleContext(SysvisParser.Attr_stmtContext, 0)

        def assignment(self):
            return self.getTypedRuleContext(SysvisParser.AssignmentContext, 0)

        def group(self):
            return self.getTypedRuleContext(SysvisParser.GroupContext, 0)

        def zone(self):
            return self.getTypedRuleContext(SysvisParser.ZoneContext, 0)

        def delete(self):
            return self.getTypedRuleContext(SysvisParser.DeleteContext, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_stmt

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt"):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)

    def stmt(self):

        localctx = SysvisParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.node_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.edge_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.attr_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.assignment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.group()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.zone()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.delete()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_list(self):
            return self.getTypedRuleContext(SysvisParser.Attr_listContext, 0)

        def GROUP(self):
            return self.getToken(SysvisParser.GROUP, 0)

        def NODE(self):
            return self.getToken(SysvisParser.NODE, 0)

        def EDGE(self):
            return self.getToken(SysvisParser.EDGE, 0)

        def ZONE(self):
            return self.getToken(SysvisParser.ZONE, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_attr_stmt

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttr_stmt"):
                return visitor.visitAttr_stmt(self)
            else:
                return visitor.visitChildren(self)

    def attr_stmt(self):

        localctx = SysvisParser.Attr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << SysvisParser.NODE) | (1 << SysvisParser.EDGE) | (1 << SysvisParser.GROUP) | (
                    1 << SysvisParser.ZONE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 60
            self.attr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_listContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SysvisParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(SysvisParser.AssignmentContext, i)

        def getRuleIndex(self):
            return SysvisParser.RULE_attr_list

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAttr_list"):
                return visitor.visitAttr_list(self)
            else:
                return visitor.visitChildren(self)

    def attr_list(self):

        localctx = SysvisParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_list)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SysvisParser.T__2)
            self.state = 63
            self.assignment()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SysvisParser.T__3:
                self.state = 64
                self.match(SysvisParser.T__3)
                self.state = 65
                self.assignment()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(SysvisParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(SysvisParser.ID)
            else:
                return self.getToken(SysvisParser.ID, i)

        def getRuleIndex(self):
            return SysvisParser.RULE_assignment

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAssignment"):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)

    def assignment(self):

        localctx = SysvisParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SysvisParser.ID)
            self.state = 74
            self.match(SysvisParser.T__5)
            self.state = 75
            self.match(SysvisParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edge_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(SysvisParser.ID)
            else:
                return self.getToken(SysvisParser.ID, i)

        def attr_list(self):
            return self.getTypedRuleContext(SysvisParser.Attr_listContext, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_edge_stmt

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEdge_stmt"):
                return visitor.visitEdge_stmt(self)
            else:
                return visitor.visitChildren(self)

    def edge_stmt(self):

        localctx = SysvisParser.Edge_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_edge_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SysvisParser.ID)
            self.state = 78
            self.match(SysvisParser.T__6)
            self.state = 79
            self.match(SysvisParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SysvisParser.T__2:
                self.state = 80
                self.attr_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SysvisParser.ID, 0)

        def attr_list(self):
            return self.getTypedRuleContext(SysvisParser.Attr_listContext, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_node_stmt

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNode_stmt"):
                return visitor.visitNode_stmt(self)
            else:
                return visitor.visitChildren(self)

    def node_stmt(self):

        localctx = SysvisParser.Node_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_node_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SysvisParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SysvisParser.T__2:
                self.state = 84
                self.attr_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(SysvisParser.GROUP, 0)

        def ID(self):
            return self.getToken(SysvisParser.ID, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(SysvisParser.Stmt_listContext, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_group

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGroup"):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)

    def group(self):

        localctx = SysvisParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SysvisParser.GROUP)
            self.state = 88
            self.match(SysvisParser.ID)
            self.state = 89
            self.match(SysvisParser.T__7)
            self.state = 90
            self.stmt_list()
            self.state = 91
            self.match(SysvisParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ZoneContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZONE(self):
            return self.getToken(SysvisParser.ZONE, 0)

        def ID(self):
            return self.getToken(SysvisParser.ID, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(SysvisParser.Stmt_listContext, 0)

        def getRuleIndex(self):
            return SysvisParser.RULE_zone

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitZone"):
                return visitor.visitZone(self)
            else:
                return visitor.visitChildren(self)

    def zone(self):

        localctx = SysvisParser.ZoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_zone)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(SysvisParser.ZONE)
            self.state = 94
            self.match(SysvisParser.ID)
            self.state = 95
            self.match(SysvisParser.T__7)
            self.state = 96
            self.stmt_list()
            self.state = 97
            self.match(SysvisParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeleteContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SysvisParser.DELETE, 0)

        def ID(self, i: int = None):
            if i is None:
                return self.getTokens(SysvisParser.ID)
            else:
                return self.getToken(SysvisParser.ID, i)

        def getRuleIndex(self):
            return SysvisParser.RULE_delete

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDelete"):
                return visitor.visitDelete(self)
            else:
                return visitor.visitChildren(self)

    def delete(self):

        localctx = SysvisParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(SysvisParser.DELETE)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(SysvisParser.ID)
                pass

            elif la_ == 2:
                self.state = 101
                self.match(SysvisParser.ID)
                self.state = 102
                self.match(SysvisParser.T__6)
                self.state = 103
                self.match(SysvisParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
