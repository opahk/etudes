defmodule EndsWith do
  def solution(str, ending) do
    ending_length = String.length(ending)
    str |> String.slice(-ending_length, ending_length)
        |> String.equivalent?(ending)
  end
end
