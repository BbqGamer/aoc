import Data.List.Split (splitOn)
import Data.Sort (sortOn)
import Data.List (tails)

data Point3D = Point3D Int Int Int
    deriving (Show, Eq)

processLine :: String -> Point3D
processLine line = 
    case map read (splitOn "," line) of
        [x, y, z] -> Point3D x y z
        _         -> error $ "Invalid line: " ++ line

dist :: Point3D -> Point3D -> Float
dist (Point3D x1 y1 z1) (Point3D x2 y2 z2) =
    sqrt (dx ^ 2 + dy ^ 2 + dz ^ 2)
    where
        dx = fromIntegral (x2 - x1)
        dy = fromIntegral (y2 - y1)
        dz = fromIntegral (z2 - z1)

main = do
    input <- getContents
    let parsed = map processLine (lines input)
    let prod = [(a, b) | (a:bs) <- tails parsed, b <- bs]
    let dists = map (uncurry dist) prod
    let sorted = sortOn snd (zip prod dists)
    print sorted