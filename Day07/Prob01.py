

class Group:

    group_header =  ""

    @classmethod
    def set_group_header(cls, gname):
        Group.group_header = gname


    @classmethod
    def get_group_header(cls):
        return Group.group_header


Group.set_group_header("Micheal Steeve")
print(Group.get_group_header())
