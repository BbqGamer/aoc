import Text.Regex.PCRE2

splitOn :: Char -> String -> [String]
splitOn _ [] = [""]
splitOn sep (x:xs)
    | x == sep = "" : splitOn sep xs
    | otherwise = let (y:ys) = splitOn sep xs in (x:y):ys

parse :: String -> (Int, Int)
parse s = let [a, b] = splitOn '-' s in (read a, read b)

sumMatching :: String -> [Int] -> Int
sumMatching regex xs = sum (filter (\n -> show n =~ regex) xs)

main :: IO ()
main = do
    content <- getLine
    let numbers = concatMap ((\(a,b) -> [a..b]) . parse) (splitOn ',' content)
    let part1 = sumMatching "^(\\d+)\\1$" numbers
    let part2 = sumMatching "^(\\d+)\\1+$" numbers
    print part1
    print part2