/** JournalBot- For use in FriendBot
 * Saves text user asks to remember, creates running log w/ time
 * @author Anish Thite, December 2016
 * @version 1.0
 * @since 12/20/2016
 */
import java.io.*;
public class JournalBot {

	private static FileOutputStream fos;
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		create_file();
	}
	/**Creates a journal (.txt file) if there exists no file
	 * @throws IOException 
	 * 
	 */
	public static void create_file() throws IOException{
		 File test = new File("C:\\Users\\anish\\Documents\\GitHub\\python\\JavaProjects\\Friend_bot\\journaltest.txt");
		 test.createNewFile();
	}
	/**appends the journal
	 *  	
	 */
	public static void append(){}
}
