from code_90_subsets_ii import Solution

def test_example_1():
    s = Solution()
    input = [4,4,4,1,4]
    output = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
    assert sorted(s.subsetsWithDup(input)) == output