import Data.List
import Data.List.Split

parse :: String -> (Int, Int)
parse line =
    case map read (splitOn "," line) of
        [x, y] -> (x, y)
        _      -> error $ "Invalid line: " ++ line

area :: (Int, Int) -> (Int, Int) -> Int
area (x1, y1) (x2, y2) = (abs (x1 - x2) + 1) * (abs (y1 - y2) + 1)

passes :: (Int, Int) -> (Int, Int) -> (Int, Int) -> (Int, Int) -> Bool
passes (x1, y1) (x2, y2) (x3, y3) (x4, y4)
    | x3 == x4 = (minX < x3 && x3 < maxX) && ((minY < y3 && y3 < maxY) || (minY < y4 && y4 < maxY) || (minY2 <= minY && maxY2 >= maxY))
    | y3 == y4 = (minY < y3 && y3 < maxY) && ((minX < x3 && x3 < maxX) || (minX < x4 && x4 < maxX) || (minX2 <= minX && maxX2 >= maxX))
    | otherwise = error "Should not happen"
    where 
        minX = min x1 x2
        maxX = max x1 x2
        minY = min y1 y2
        maxY = max y1 y2
        minX2 = min x3 x4
        maxX2 = max x3 x4
        minY2 = min y3 y4
        maxY2 = max y3 y4

valid edges (a, b) =
    not (any (\(p1, p2) -> passes a b p1 p2) edges)

argmax :: Ord b => (a -> b) -> [a] -> a
argmax f = maximumBy (\x y -> compare (f x) (f y))

main = do
    input <- map parse <$> lines <$> getContents
    let edges = zip input (tail (input ++ ([head input])))
    let squares = [ (a, b) | (a:rest) <- tails input, b <- rest ]
    let filtered = filter (valid edges) squares
    print (maximum (map (uncurry area) filtered))
    print (argmax (uncurry area) filtered)
