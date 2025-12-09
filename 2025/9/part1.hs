import Data.List
import Data.List.Split

parse :: String -> (Int, Int)
parse line =
    case map read (splitOn "," line) of
        [x, y] -> (x, y)
        _      -> error $ "Invalid line: " ++ line

area :: (Int, Int) -> (Int, Int) -> Int
area (x1, y1) (x2, y2) = (abs (x1 - x2) + 1) * (abs (y1 - y2) + 1)

main = do
    input <- map parse <$> lines <$> getContents
    print (maximum [ area a b | (a:rest) <- tails input, b <- rest ])
