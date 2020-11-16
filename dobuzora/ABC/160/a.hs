checkCoffee :: String -> String
checkCoffee x = if check
                then "Yes"
                else "No"
  where front = (x!!2 == x!!3)
        back = (x!!4 == x!!5)
        check = (front && back)

main :: IO ()
main = do
  n <- getLine
  putStrLn (checkCoffee n)
