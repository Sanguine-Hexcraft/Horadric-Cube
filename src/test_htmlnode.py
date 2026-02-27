import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "id": "main"},
        )

        self.assertEqual(node.props_to_html(), ' class="greeting" id="main"')

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_values(self):
        node = LeafNode(
            "div",
            "this is the end",
            {"class": "primary"}
        )

        self.assertEqual(node.to_html(), '<div class="primary">this is the end</div>')

    def test_left_no_tag(self):
        node = LeafNode(None, "this is the end")

        self.assertEqual(node.to_html(), "this is the end")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_tag(self):
        node = ParentNode(None, [LeafNode(None, "x")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_child(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_empty_child(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_multiple_children(self):
        node = ParentNode(
            "div", [
            LeafNode(None, "a"),
            LeafNode("b", "b"),
            LeafNode(None, "c"),
        ])
        self.assertEqual(node.to_html(), "<div>a<b>b</b>c</div>")
                         
    def test_parent_props_render(self):
        node = ParentNode("div", [LeafNode(None, "test")], {"class": "primary"})
        self.assertEqual(node.to_html(), '<div class="primary">test</div>')

    def test_parent_deep_nesting(self):
        node = ParentNode("div", [
            ParentNode("p", [
                ParentNode(
                    "b", [
                        LeafNode(None, "test")
                    ]
                )
            ])
        ])
        self.assertEqual(node.to_html(), "<div><p><b>test</b></p></div>")

    def test_parent_repr(self):
        node = ParentNode("p", [LeafNode("span", "test")], {"class": "primary"})
        expected = "ParentNode(p, children: [LeafNode(span, test, None)], {'class': 'primary'}"
        self.assertEqual(repr(node), expected)

