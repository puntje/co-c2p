from compiler.ASTNode import ASTNode
from compiler.types.VoidType import VoidType
from compiler.MyErrorListener import C2PException
from grammar.SmallCParser import SmallCParser


class VariableDeclaration(ASTNode):

    def __init__(self, environment, typename, var_decl_list):
        super().__init__(environment, SmallCParser.VARIABLEDECLARATION)

        if isinstance(typename, VoidType):
            raise C2PException("variable has incomplete type 'void'")

        self.typename = typename
        self.variable_identifiers = var_decl_list

        for var in self.variable_identifiers.variable_ids:
            if var.identifier not in environment.symbol_table.stack[-1]:
                var.setType(typename)
                self.addChild(var)
            else:
                raise C2PException("redefinition of '" + var.identifier + "'")

    def getDeclarationSize(self):
        space = 0

        for var_id in self.variable_identifiers.variable_ids:
            space += var_id.getSize()

        return space

    def getDisplayableText(self):
        return "var decl"

    def generateCode(self, out):
        self.variable_identifiers.generateCode(out)
