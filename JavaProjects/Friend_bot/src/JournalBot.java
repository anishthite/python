/** JournalBot- For use in FriendBot
 * Saves text user asks to remember, creates running log w/ time
 * @author Anish Thite, December 2016
 * @version 1.0
 * @since 12/20/2016
 */
import java.io.*;
public class JournalBot {

	private static FileWriter fw;
	private static BufferedWriter writer;
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args)  {
		create_journal("test");
	}
	/**Creates a journal (.txt file)
	 * @throws IOException 
	 * 
	 */
	public static void create_journal(String journalName) {
		try { 
		File journal = new File("C:\\Users\\anish\\Documents\\journals\\" + journalName + ".txt");	
		
		if (journal.createNewFile()){
			
			
		}
		else{
			
			
		}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	/**appends the journal
	 *  	
	 */
	public static void write(String text, String journalName){
		
		fw = new FileWriter("C:\\Users\\anish\\Documents\\journals\\" + journalName + ".txt");
		writer = new BufferedWriter(fw);
		
		
	}
}
