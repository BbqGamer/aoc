import Data.List.Split (splitOn)
import Data.Sort (sort, sortOn)
import Data.List (tails, group)
import qualified Data.Map as Map
import System.Environment (getArgs)

data Point3D = Point3D Int Int Int
    deriving (Show, Eq, Ord)

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

buildGraph :: Map.Map Point3D Int -> Int -> [((Point3D, Point3D), Float)] -> Map.Map Point3D Int
buildGraph pointMap _ [] = pointMap
buildGraph pointMap 0 _ = pointMap
buildGraph pointMap n (((a,b), _) : points) =
    res
    where
        ma = Map.lookup a pointMap
        mb = Map.lookup b pointMap
        res = case (ma, mb) of
            (Nothing, Nothing)      -> buildGraph (Map.insert b n (Map.insert a n pointMap)) (n-1) points
            (Nothing, Just mbVal)   -> buildGraph (Map.insert a mbVal pointMap) (n - 1) points
            (Just maVal, Nothing)   -> buildGraph (Map.insert b maVal pointMap) (n - 1) points
            (Just maVal, Just mbVal) -> if maVal == mbVal then buildGraph pointMap (n - 1) points else buildGraph (Map.map (\v -> if v == mbVal then maVal else v) pointMap) (n-1) points

main = do
    input <- getContents
    args <- getArgs
    let n = read (head args) :: Int
    let parsed = map processLine (lines input)
    let prod = [(a, b) | (a:bs) <- tails parsed, b <- bs]
    let dists = map (uncurry dist) prod
    let sorted = sortOn snd (zip prod dists)
    let res = buildGraph Map.empty n sorted
    print (sort (Map.elems res))
    print (product (take 3 (reverse (sort (map length (group (sort (Map.elems res))))))))