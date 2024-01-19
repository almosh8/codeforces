import java.util.TreeMap

// Function to read a line from stdin and return it
fun getLine(): String {
    return readLine() ?: throw IllegalArgumentException("Input cannot be null")
}

// Function to read a line from stdin, split it by spaces, and return an array of strings
fun getStringsArray(): Array<String> {
    return (readLine() ?: throw IllegalArgumentException("Input cannot be null"))
        .split(" ").toTypedArray()
}

// Function to read a line from stdin, split it by spaces, and return an array of ints
fun getIntsArray(): IntArray {
    return (readLine() ?: throw IllegalArgumentException("Input cannot be null"))
        .split(" ").map { it.toInt() }.toIntArray()
}

// Function to read a line from stdin, convert it to int, and return the int
fun getInt(): Int {
    return (readLine() ?: throw IllegalArgumentException("Input cannot be null"))
        .toIntOrNull() ?: throw NumberFormatException("Invalid integer format")
}


fun main(args: Array<String>) {

  
   

}
