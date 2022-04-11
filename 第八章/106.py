import re


def analyze(l_html: list):
    outer_compare = re.compile(r"<\w*>")
    inner_compare = re.compile(r">.*<")
    out = {}
    for l in l_html:
        # print(outer_compare.match(l))
        # print(inner_compare.findall(l))
        key = l[outer_compare.match(l).start() + 1: outer_compare.match(l).end() - 1]
        value = inner_compare.findall(l)[0][1:-1]
        out[key] = value
        # print(key)
    return out


if __name__ == "__main__":
    html = ["<composer>Wolfgang Amadeus Mozart</composer>",
            "<author>Samuel Beckett</author>",
            "<city>London</city>"]
    analyzed = analyze(html)
    for i in analyzed.keys():
        print(i + ":", analyzed[i])
