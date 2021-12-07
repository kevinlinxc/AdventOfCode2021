// This object-based implementation would have been more useful if the question actually included diagonal bingos, but
// it didn't so all around this was not an optimal implementaiton. However, it was an excellent reminder of how
// objects in Java so it was fine.
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.toList;

public class Day4 {
    public static void main(String[] args) {
        List<String> listInput = loadInput();
        String[] bingoNums = listInput.get(0).split(",");
        System.out.println("Numbers to call: " + Arrays.toString(bingoNums));
        List<BingoGrid> grids = new ArrayList<>();
        int gridCounter = 0;
        for (int i = 2; i < listInput.size(); i+=6) {
            BingoGrid newgrid = new BingoGrid(listInput.subList(i, i + 5), gridCounter);
            System.out.println("Adding " + newgrid);
            grids.add(newgrid);
            gridCounter += 1;
        }

        List<String> calledSoFar = new ArrayList<>();
        for (String bingoNum: bingoNums){
            System.out.println("Calling: " + bingoNum);
            calledSoFar.add(bingoNum);
            for (BingoGrid grid : grids){
                boolean bingo = grid.updateGrid(bingoNum);
                if (bingo){
                    System.out.println(grid.getScore(bingoNum));
                    return;
                }
            }
            System.out.println("Called so far: "+ calledSoFar);
        }

    }

    public static List<String> loadInput() {
        String fileName = "inputs\\day4.txt";
        try (BufferedReader r = new BufferedReader(new InputStreamReader(new FileInputStream(fileName)))) {
            return r.lines().collect(toList());
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }

    static class BingoGrid {
        private final BingoNode[][] grid;
        private static final int width = 5;
        private static final int height = 5;
        public final int index;

        static class BingoNode {
            private final String value;
            private boolean called;


            public BingoNode(String value) {
                this.called = false;
                this.value = value;
            }

            public boolean isCalled() {
                return called;
            }

            public void setCalled(boolean called) {
                this.called = called;
            }

            @Override
            public String toString() {
                return value+ ": " + called;
            }
        }

        public BingoGrid(List<String> rows, int index) {
            this.index = index;
            // populate grid
            this.grid = new BingoNode[width][height];
            for (int i = 0; i < rows.size(); i ++){
                String[] columnsArr = rows.get(i).split("[ ]{1,}");
                List<String> columns = new LinkedList<>(Arrays.asList(columnsArr));
                columns.removeAll(Collections.singleton(""));
                ListIterator<String> columnsIt = columns.listIterator();
                while (columnsIt.hasNext()){ // like enumerate in Python, but worse
                    int j = columnsIt.nextIndex();
                    String value = columnsIt.next();
                    this.grid[i][j] = new BingoNode(value);
                }
            }
        }

        public List<BingoNode> getNodes(){
            return Arrays.stream(this.grid).flatMap(Arrays::stream).collect(Collectors.toList());
        }

        public boolean BINGO(){
            boolean bingoFound = this.rowBINGO() || this.columnBINGO(); // || this.diagonalBINGO()
            if (bingoFound){
                System.out.println("BINGO IN GRID: " + index);
            }
            return bingoFound;
        }

        public boolean rowBINGO(){
            for (int i = 0; i < height; i++){
                boolean rowGood = true;
                for (int j = 0; j < width; j++){
                    if (!this.grid[i][j].isCalled()) {
                        rowGood = false;
                        break;
                    }
                }
                if (rowGood){
                    return true;
                }
            }
            return false;
        }

        public boolean columnBINGO(){
            for (int j = 0; j < width; j++){
                boolean columnGood = true;
                for (int i = 0; i < height; i++){
                    if (!this.grid[i][j].isCalled()){
                        columnGood = false;
                        break;
                    }
                }
                if (columnGood){
                    return true;
                }
            }
            return false;
        }

        public boolean diagonalBINGO(){
            boolean mainDiagGood = true;
            for (int i = 0; i < width; i++){
                if (!this.grid[i][i].isCalled()) {
                    mainDiagGood = false;
                    break;
                }
            }
            if (mainDiagGood){
                return true;
            }
            boolean secDiagGood = true;
            for (int i = width-1; i >0; i--){
                if (!this.grid[i][width - i].isCalled()) {
                    secDiagGood = false;
                    break;
                }
            }
            if (secDiagGood){
                return true;
            }
            return false;
        }

        public boolean updateGrid(String value){
            for (int i = 0; i < width; i++){
                for (int j = 0; j < height; j++){
                    if (this.grid[i][j].value.equals(value)){
                        System.out.println("Marking " + value + " on grid " + index);
                        this.grid[i][j].setCalled(true);
                        if (this.BINGO()) {
                            return true;
                        } else {
                            return false;
                        }
                    }
                }
            }
            return false;
        }

        public int getScore(String called){
            int unmarked = 0;
            List<BingoNode> nodes = this.getNodes();
            for (BingoNode x: nodes){
                if (!x.isCalled()){
                    unmarked = unmarked + Integer.parseInt(x.value);
                }
            }
            System.out.println("Called: " + called + " Unmarked total: " + unmarked);
            int result = Integer.parseInt(called) * unmarked;
            System.out.println("Final answer: " + result);
            System.out.println("Grid: " + this);
            return result;
        }

        @Override
        public String toString() {
            return this.getNodes().toString();
        }
    }

}

//10374