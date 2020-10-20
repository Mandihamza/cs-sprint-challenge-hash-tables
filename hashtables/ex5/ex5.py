def finder(files, queries):
    queries_cache = {}
    for path in files:
        file_item = path.split('/')[-1]

        if file_item in queries_cache:
            queries_cache[file_item].append(path)
        else:
            queries_cache[file_item] = [path]

    result = []
    for query in queries:
        if query in queries_cache:
            results = queries_cache[query]
            for path in results:
                result.append(path)
    return result


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
