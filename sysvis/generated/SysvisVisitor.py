# Generated from Sysvis.g4 by ANTLR 4.7.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .SysvisParser import SysvisParser
else:
    from SysvisParser import SysvisParser


# This class defines a complete generic visitor for a parse tree produced by SysvisParser.

class SysvisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SysvisParser#story.
    def visitStory(self, ctx: SysvisParser.StoryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#moment.
    def visitMoment(self, ctx: SysvisParser.MomentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#stmt_list.
    def visitStmt_list(self, ctx: SysvisParser.Stmt_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#stmt.
    def visitStmt(self, ctx: SysvisParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#attr_stmt.
    def visitAttr_stmt(self, ctx: SysvisParser.Attr_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#attr_list.
    def visitAttr_list(self, ctx: SysvisParser.Attr_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#assignment.
    def visitAssignment(self, ctx: SysvisParser.AssignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#edge_stmt.
    def visitEdge_stmt(self, ctx: SysvisParser.Edge_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#node_stmt.
    def visitNode_stmt(self, ctx: SysvisParser.Node_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#group.
    def visitGroup(self, ctx: SysvisParser.GroupContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#zone.
    def visitZone(self, ctx: SysvisParser.ZoneContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SysvisParser#delete.
    def visitDelete(self, ctx: SysvisParser.DeleteContext):
        return self.visitChildren(ctx)


del SysvisParser
