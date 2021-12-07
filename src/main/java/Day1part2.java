import java.io.*;
import java.util.List;

import static java.util.stream.Collectors.toList;

public class Day1part2 {
    public static void main(String[] args) {
        List<String> listInput = loadInput();
        int last = Integer.parseInt(listInput.get(0)) + Integer.parseInt(listInput.get(1)) + Integer.parseInt(listInput.get(2));
        int current;
        int counter = 0;
        for (int i = 1; i < listInput.size() - 2; i++){
            current = Integer.parseInt(listInput.get(i)) + Integer.parseInt(listInput.get(i+1)) + Integer.parseInt(listInput.get(i+2));
            if (current > last){
                counter += 1;
            }
            last = current;
        }
        System.out.println(counter);

    }

    public static List<String> loadInput(){
        String fileName = "inputs\\day1.txt";
        try(BufferedReader r = new BufferedReader(new InputStreamReader(new FileInputStream(fileName)))){
            return r.lines().collect(toList());
        } catch(IOException e){
            throw new UncheckedIOException(e);
        }
    }
}
// 1743
