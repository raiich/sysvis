grammar Sysvis;

story: moment ('---' moment)* '---'? EOF;
moment: stmt_list ;

stmt_list: stmt (';' stmt)* ';'? ;
stmt: node_stmt
    | edge_stmt
    | attr_stmt
	| assignment
    | group
    | zone
    | delete
    ;

attr_stmt : (GROUP | NODE | EDGE | ZONE) attr_list ;
attr_list : '[' assignment ( ( ',' | ';' )?  assignment)* ']' ;
assignment : ID '=' ID ;

edge_stmt : ID '->' ID attr_list? ;

node_stmt : ID attr_list? ;

group : GROUP ID '{' stmt_list '}' ;
zone  : ZONE  ID '{' stmt_list '}' ;

delete: DELETE (ID | ID '->' ID);

NODE : 'node' ;
EDGE : 'edge' ;
GROUP: 'group' ;
ZONE : 'zone' ;
DELETE: 'delete' ;

ID : '\'' (~'\'')* '\'' {self.text = self.text[1:-1]}
   | '"' (~'"')* '"' {self.text = self.text[1:-1]}
   | [a-zA-Z_0-9\-] [a-zA-Z_0-9.\-]*
   ;

SPACES : [ \u000B\t\r\n] -> channel(HIDDEN) ;
