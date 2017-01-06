/** JournalBot- For use in FriendBot
 * Saves text user asks to remember, creates running log w/ time
 * @author Anish Thite, December 2016
 * @version 1.1
 * @since 12/20/2016
 */
import java.io.*;
public class JournalBot {

	private static FileWriter fw;
	private static BufferedWriter writer;
	public static File journal;
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args)  {
		open_journal("test");
	}
	/**Creates a journal (.txt file)
	 *  @returns journal
	 * 
	 */
	public static File open_journal(String journalName) {
		try { 
			File journal = new File("C:\\Users\\anish\\Documents\\journals\\" + journalName + ".txt");		
			if (!journal.exists()){
				journal.createNewFile();	
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		return journal;
	}
	/**appends the journal
	 *  	
	 */
	public static void write(String text, String journalName){
		
		try {
			fw = new FileWriter(journal.getAbsoluteFile(), true);
			writer = new BufferedWriter(fw);
			writer.write(text);
			System.out.println("Appended to journal");
		} 
		catch (IOException e) {
			e.printStackTrace();
		}
	}
}
