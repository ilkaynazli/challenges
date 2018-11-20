"""Find 'cousin' nodes -- those nodes at the same level as a node.

Consider the tree::

            a
        ---------
       /    |    \
      b     c     d
     /-\   /-\   /-\
    e  f  g  h  i  j
        \     \
        k     l

Nodes `k` and `l` are at same level ("cousins", a we'll call them, but removed
by several levels). Similarly `e`, `f`, `g`, `h`, `i`, and `j` are cousins, as are
`b`, `c`, and `d`.

Let's create this tree::

    >>> a = Node("a")

    >>> b = Node("b")
    >>> c = Node("c")
    >>> d = Node("d")
    >>> b.set_parent(a)
    >>> c.set_parent(a)
    >>> d.set_parent(a)

    >>> e = Node("e")
    >>> f = Node("f")
    >>> g = Node("g")
    >>> h = Node("h")
    >>> i = Node("i")
    >>> j = Node("j")
    >>> e.set_parent(b)
    >>> f.set_parent(b)
    >>> g.set_parent(c)
    >>> h.set_parent(c)
    >>> i.set_parent(d)
    >>> j.set_parent(d)

    >>> k = Node("k")
    >>> l = Node("l")
    >>> k.set_parent(f)
    >>> l.set_parent(h)

Let's find the cousins for b::

    >>> b.cousins() == {c, d}
    True

    >>> c.cousins() == {b, d}
    True

    >>> e.cousins() == {f, g, h, i, j}
    True

    >>> k.cousins() == {l}
    True

The root node has no cousins::

    >>> a.cousins() == set()
    True
"""


class Node(object):
    """Doubly-linked node in a tree.

        >>> na = Node("na")
        >>> nb1 = Node("nb1")
        >>> nb2 = Node("nb2")

        >>> nb1.set_parent(na)
        >>> nb2.set_parent(na)

        >>> na.children
        [<Node nb1>, <Node nb2>]

        >>> nb1.parent
        <Node na>
    """

    parent = None

    def __init__(self, data):
        self.children = []
        self.data = data

    def __repr__(self):
        return "<Node %s>" % self.data

    def set_parent(self, parent):
        """Set parent of this node.

        Also sets the children of the parent to include this node.
        """

        self.parent = parent
        parent.children.append(self)

    def cousins(self):
        """Find nodes on the same level as this node."""
        """
            We need to do breadth first search
            append children of parent to a set
            if more than one parent in one level loop through them (cousins of cousins)
            return the set

        """
        if self is None or self.parent is None:
            return set()

        current = self
        while current.parent:
            current = current.parent

        siblings = [current]

        while siblings:
            if self in siblings:
                siblings.remove(self)
                return set(siblings)

            new_siblings = []
            for sibling in siblings:
                new_siblings.extend(sibling.children)

            siblings = new_siblings[:]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB! ***\n")