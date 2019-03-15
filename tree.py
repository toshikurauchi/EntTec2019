from collections import deque


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return None
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = Node(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]

    @property
    def height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return -1
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return max(left_height, right_height) + 1

    def to_representation(self):
        total_full = 2**(self.height+1)-1  # Number of nodes in the full tree
        representation = []
        q = deque([self.root])
        i = 0
        last_node = -1
        while q and i < total_full:
            node = q.popleft()
            value = None
            left, right = None, None
            if node:
                left = node.left
                right = node.right
                value = node.value
                last_node = i
            q.append(left)
            q.append(right)
            representation.append(value)

            i += 1
        return representation[:last_node+1]

    def __str__(self):
        VALUE_SIZE = 3
        VALUE_FORMAT = '{:^' + str(VALUE_SIZE) + 'd}'
        LEFT_ARROW = '  /'
        RIGHT_ARROW = '\\  '
        representation = self.to_representation()
        height = self.height
        lines = []
        outer = 0
        inner = 1
        prev_h_line = (2**(height+1)-1)*VALUE_SIZE*' '
        for level in range(height, -1, -1):
            first = True
            outer_spaces = VALUE_SIZE * outer * ' '
            inner_spaces = VALUE_SIZE * inner * ' '
            line = outer_spaces
            arrows_line = outer_spaces
            h_line = (2**(height+1)-1)*VALUE_SIZE*' '
            for i in range(2**level-1, 2**(level+1)-1):
                value_str = VALUE_SIZE * ' '
                arrows_str = value_str
                h_start_add = None
                h_end_add = None
                if i < len(representation) and representation[i] is not None:
                    value_str = (VALUE_FORMAT).format(representation[i])
                    if i % 2 == 1:
                        arrows_str = LEFT_ARROW
                        h_start_add = VALUE_SIZE
                        h_end_add = h_start_add+outer*VALUE_SIZE+VALUE_SIZE//2
                    else:
                        arrows_str = RIGHT_ARROW
                        h_start_add = -(outer+1)*VALUE_SIZE+VALUE_SIZE//2
                        h_end_add = 0
                if first:
                    first = False
                else:
                    arrows_line += inner_spaces
                    line += inner_spaces
                if h_start_add is not None and h_end_add is not None:
                    h_start = len(arrows_line) + h_start_add
                    h_end = len(arrows_line) + h_end_add
                    h_line = _insert_str(h_line, '_', h_start, h_end)
                arrows_line += arrows_str
                line += value_str
            line += outer_spaces
            arrows_line += outer_spaces
            line = _merge_lines(line, prev_h_line)
            prev_h_line = h_line
            lines.append(line)
            if level > 0:
                lines.append(arrows_line)
            outer = inner
            inner = 2*inner+1
        remove_left = min([len(line)-len(line.lstrip()) for line in lines])
        remove_right = min([len(line)-len(line.rstrip()) for line in lines])
        lines = [line[remove_left:-remove_right] for line in lines]
        return '\n'.join(reversed(lines))


def _insert_str(string, char, start_pos, end_pos):
    replacement = char * (end_pos - start_pos)
    return string[:start_pos] + replacement + string[end_pos:]


def _merge_lines(line, h_line):
    for i, (c_line, c_h_line) in enumerate(zip(line, h_line)):
        if len(c_line.strip()) == 0:
            line = line[:i] + c_h_line + line[i+1:]
    return line


if __name__ == "__main__":
    print(Tree(list(range(12))))
