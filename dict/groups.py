def groups_per_user(group_dictionary):
    user_groups = {}
    a = { y:x for x:y in group_dictionary.iteritems()}
    # for group, users in group_dictionary.items():
    #     for user in users:
    #         user_groups[user] = []

        # if not group in group_dictionary.values():
        #     user_groups[user].append(group)
        # for user, groups in user_groups.items():

            # if not group in user_groups[user]:

    # return(user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))
