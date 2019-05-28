defmodule EndsWith do
  def solution(str, ending) do
    ending_length = String.length(ending)
    if ending_length == 0 do
      true
    else
      String.slice(str, -ending_length..-1) == ending
    end
  end
end
