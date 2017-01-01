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
		create_journal("test");
	}
	/**Creates a journal (.txt file)
	 * @throws IOException 
	 * 
	 */
	public static void create_journal(String journalName) throws IOException{
		 File test = new File("C:\\Users\\anish\\Documents\\journals\\" + journalName + ".txt");
		 test.createNewFile();
	}
	/**appends the journal
	 *  	
	 */
	public static void write(String text, String journalName){
		FileOutputStream 
	}
}
