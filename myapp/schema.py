import graphene

class Query(graphene.ObjectType):
    analyze=graphene.String(sentence=graphene.String(required=True))

    def resolve_analyze(self, info, sentence):
        # call the function that analyzes the sentence
        return f'analysis of {sentence}'

schema = graphene.Schema(query=Query)