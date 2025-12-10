import           Control.Applicative (some)
import           Data.Void
import           Text.Megaparsec
import           Text.Megaparsec.Char
import qualified Text.Megaparsec.Char.Lexer as L

type Parser = Parsec Void String

data Machine = Machine
  { lights :: String
  , buttons :: [[Int]]
  , joltage :: [Int]
  } deriving (Show)

buttonP :: Parser [Int]
buttonP = between (char '(') (char ')') (L.decimal `sepBy` char ',')

parseMachine :: Parser Machine
parseMachine = do
  l <- between (char '[') (char ']') (many (noneOf "]"))
  space
  bs <- many (buttonP <* space)
  j <- between (char '{') (char '}') (L.decimal `sepBy` char ',')
  eof
  return (Machine l bs j)

main :: IO ()
main = do
    input <- lines <$> getContents
    let parsed = map (runParser (parseMachine <* eof) "") input
    print parsed
