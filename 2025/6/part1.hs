import Data.List (transpose)

calc :: [String] -> Int
calc ("+":xs) = sum (map read xs)
calc ("*":xs) = product (map read xs)
calc _ = 0

main :: IO ()
main = do
    input <- transpose . map words . reverse . lines <$> getContents
    print $ sum (map calc input)