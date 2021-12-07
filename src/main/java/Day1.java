import java.io.*;
import java.util.List;

import static java.util.stream.Collectors.toList;

public class Day1 {
    public static void main(String[] args) {
        List<String> listInput = loadInput();
        String last = listInput.get(0);
        String current;
        int counter = 0;
        for (int i = 1; i < listInput.size(); i++){
            current = listInput.get(i);
            if (Integer.parseInt(current) > Integer.parseInt(last)){
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

// 1711
