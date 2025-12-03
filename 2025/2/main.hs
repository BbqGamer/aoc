splitOn :: Char -> String -> [String]
splitOn _ [] = [""]
splitOn sep (x:xs)
    | x == sep = "" : splitOn sep xs
    | otherwise = let (y:ys) = splitOn sep xs in (x:y):ys

parse :: String -> (Int, Int)
parse s = let [a, b] = splitOn '-' s in (read a, read b)

main :: IO ()
main = do
    content <- getLine
    let ranges = concatMap ((\(a,b) -> [a..b]) . parse) (splitOn ',' content)
    print ranges