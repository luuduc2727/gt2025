def path_exists(graph, start, end):
    node_checked = set()

    # Depth-First Search
    def Depth_First_Search(node):
        if node == end:
            return True
        node_checked.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in node_checked:
                if Depth_First_Search(neighbor):
                    return True
        return False

    return Depth_First_Search(start)


def main():
    # Graph
    graph = {
        '1': ['2'],
        '2': ['1', '5'],
        '3': ['6'],
        '4': ['6', '7'],
        '5': ['2'],
        '6': ['3', '4', '7'],
        '7': ['4', '6']
    }

    print("Enter the start and end nodes:")
    start = input("Start node: ").strip()
    end = input("End node: ").strip()

    if path_exists(graph, start, end):
        print(f"=> Path exists between {start} and {end}.")
    else:
        print(f"=> No path exists between {start} and {end}.")


if __name__ == "__main__":
    main()
