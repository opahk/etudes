defmodule TestSolution do
  use ExUnit.Case
  import EndsWith, only: [solution: 2]

  test "solution" do
    assert solution("abc", "bc") == true
    assert solution("abc", "d") == false
    assert solution("abc", "c") == true
    assert solution("abc", "") == true
    assert solution("", "") == true
    assert solution("a", "") == true
    assert solution("abcd", "abcd") == true
  end
end
