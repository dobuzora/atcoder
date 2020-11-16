-- A - ABC Swap

originSplit :: [Char] -> [Char] -> [[Char]]
originSplit n [] = reverse n : []
originSplit n (x:xs) = if x == ' '
                       then reverse n : originSplit "" xs
                       else originSplit (x : n) xs

doProcess input = input!!2 ++ " " ++ input!!0 ++ " " ++ input!!1

main :: IO ()
main = do
  n <- getLine
  let input = originSplit "" n
  putStrLn (doProcess input)
