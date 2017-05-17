class Model:
    def __init__(self):
        self.id = ""
        self.parent_id = ""
        self.message = ""
        self.author_id = ""
        self.author_name = ""
        self.date = ""
        pass

    @staticmethod
    def from_youtube(obj):
        snippet = obj['snippet']
        if 'topLevelComment' in snippet:
            comment_snippet = snippet['topLevelComment']['snippet']
        else:
            comment_snippet = snippet

        i = Model()
        i.id = obj['id']
        if 'videoId' in snippet:
            i.parent_id = snippet['videoId']
        else:
            i.parent_id = snippet['parentId']
        i.message = comment_snippet['textOriginal']
        i.author_id = comment_snippet['authorChannelId']['value']
        i.author_name = comment_snippet['authorDisplayName']
        i.date = comment_snippet['updatedAt']

        return i

    def to_dic(self):
        data = {}
        for key in self.__dict__.keys():
            data[key] = getattr(self, key, None)
        return data

    def __repr__(self):
        return str(self.to_dic())
