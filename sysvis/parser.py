from antlr4 import CommonTokenStream, InputStream

from sysvis.generated import SysvisParser, SysvisLexer, SysvisVisitor
from sysvis.models import (
    Moment, Story, Attribute, Edge, Node, Group, Assignment, StatementList, Zone, DeleteMob, DeleteEdge
)


def parse(statement):
    input_stream = InputStream(statement)
    visitor = SysvisConstructor()
    lexer = SysvisLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SysvisParser(token_stream)
    tree = parser.story()
    return visitor.visit(tree)


class SysvisConstructor(SysvisVisitor):
    def visitStory(self, ctx: SysvisParser.StoryContext):
        if ctx.EOF():
            return Story([self.visit(moment) for moment in ctx.moment()])
        else:
            raise SyntaxError('invalid input statement syntax')

    def visitMoment(self, ctx: SysvisParser.MomentContext):
        def moment(s: StatementList):
            return Moment(s.setups, s.attributes, **s.assignments)
        return moment(self.visit(ctx.stmt_list()))

    def visitStmt_list(self, ctx: SysvisParser.Stmt_listContext):
        return StatementList.of([self.visit(stmt) for stmt in ctx.stmt()])

    def visitStmt(self, ctx: SysvisParser.StmtContext):
        return self.visit(
            ctx.node_stmt() or
            ctx.edge_stmt() or
            ctx.attr_stmt() or
            ctx.assignment() or
            ctx.zone() or
            ctx.group() or
            ctx.delete()
        )

    def visitAttr_stmt(self, ctx: SysvisParser.Attr_stmtContext):
        attr_type = ctx.GROUP() or ctx.NODE() or ctx.EDGE() or ctx.ZONE()
        attr_list = ctx.attr_list()
        assignments = {}
        if attr_list:
            assignments = self.visit(attr_list)
        return Attribute(attr_type.getText(), **assignments)

    def visitAttr_list(self, ctx: SysvisParser.Attr_listContext):
        assignments = [self.visit(assignment) for assignment in ctx.assignment()]
        return {a.key: a.value for a in assignments}

    def visitAssignment(self, ctx: SysvisParser.AssignmentContext):
        ids = ctx.ID()
        ids = list(map(lambda x: x.getText(), ids))
        return Assignment(ids[0], ids[1])

    def visitEdge_stmt(self, ctx: SysvisParser.Edge_stmtContext):
        ids = ctx.ID()
        ids = list(map(lambda x: x.getText(), ids))
        attr_list = ctx.attr_list()
        return Edge(ids[0], '->', ids[1], **self.visit(attr_list) if attr_list else {})

    def visitNode_stmt(self, ctx: SysvisParser.Node_stmtContext):
        attr_list = ctx.attr_list()
        kwargs = self.visit(attr_list) if attr_list else {}
        return Node(ctx.ID().getText(), **kwargs)

    def visitGroup(self, ctx: SysvisParser.GroupContext):
        def group(gid: str, s: StatementList):
            return Group(gid, s.setups, s.attributes, **s.assignments)
        stmt_list = ctx.stmt_list()
        statements = self.visit(stmt_list) if stmt_list else []
        return group(ctx.ID().getText(), statements)

    def visitZone(self, ctx: SysvisParser.ZoneContext):
        def zone(zid: str, s: StatementList):
            return Zone(zid, s.setups, s.attributes, **s.assignments)
        stmt_list = ctx.stmt_list()
        statements = self.visit(stmt_list) if stmt_list else []
        return zone(ctx.ID().getText(), statements)

    def visitDelete(self, ctx: SysvisParser.DeleteContext):
        ids = list(map(lambda x: x.getText(), ctx.ID()))
        if len(ids) == 1:
            return DeleteMob(ids[0])
        elif len(ids) == 2:
            return DeleteEdge(ids[0], ids[1])
        else:
            raise NotImplementedError
