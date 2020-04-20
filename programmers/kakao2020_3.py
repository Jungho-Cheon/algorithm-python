# Trie 구조 사용
class Node(object):

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self, words):
        self.root = Node(None)
        self.root_backword = Node(None)
        self.word_len = {}
        for word in words:
            self.insert(True, word)
            self.insert(False, word[::-1])
            if len(word) not in self.word_len:
                self.word_len[len(word)] = 1
            else:
                self.word_len[len(word)] += 1

    def insert(self, direction, word):
        if direction:
            curr_node = self.root
        else:
            curr_node = self.root_backword

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node(c)

            curr_node = curr_node.children[c]

        curr_node.data = word

    def starts_with(self, direction, prefix, length):
        if direction:
            curr_node = self.root
        else:
            curr_node = self.root_backword

        result = []
        subtrie = None
        depth = 0

        for c in prefix:
            if length < depth:
                break
            if c in curr_node.children:
                curr_node = curr_node.children[c]
                subtrie = curr_node
                depth += 1
            else:
                return []

        Q = list(subtrie.children.values())

        while Q:
            curr = Q.pop(0)
            if curr.data != None and len(curr.data) == length:
                result.append(curr.data)

            Q += list(curr.children.values())

        return result


def solution(words, queries):
    MAX = max([len(query) for query in queries])
    words = [w for w in words if len(w) <= MAX]
    t = Trie(words)
    d = dict()
    answer = []
    for query in queries:
        if query in d:
            answer.append(d[query])
            continue

        token = query.split('?')
        query_len = len(query)
        if query[0] == '?' and query[-1] != '?':
            count = len(t.starts_with(False, token[-1][::-1], query_len))

        elif query[0] != '?' and query[-1] == '?':
            count = len(t.starts_with(True, token[0], query_len))

        else:
            if query_len in t.word_len:
                count = t.word_len[query_len]
            else:
                count = 0

        d[query] = count
        answer.append(count)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
