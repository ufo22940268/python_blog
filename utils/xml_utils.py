def get_class(node):
    if not node: 
        return None;

    node_map = node.attributes;
    for i in range(node_map.length):
        item = node_map.item(i)
        if item.name == "class":
            return item.value;

    return None;
