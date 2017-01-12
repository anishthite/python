/** JournalBot- For use in FriendBot
 * Saves text user asks to remember, creates running log w/ time
 * @author Anish Thite, December 2016
 * @version 1.1
 * @since 12/20/2016
 */
import java.io.*;
import java.time.LocalDateTime;
public class JournalBot {

	public static FileWriter fw;
	public static BufferedWriter writer;
	public static File journal;
	/**
	 * @param args
	 *  
	 */
	public static void main(String[] args)  {
		open_journal("test");
	}
	/**Creates a journal (.txt file)
	 *  @param journalName- journal name in string input
	 *  @returns journal- .txt file here user saves string text
	 * 
	 */
	public static File open_journal(String journalName) {
		try { 
			File journal = new File("..\\bin\\journals\\" + journalName + ".txt");		
			if (!journal.exists()){
				journal.createNewFile();	
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		return journal;
	}
	/**appends the journal with input text, and adds date/time to it
	 *  @param text- text user wants to input to journal 
	 *  @param journalName- name of journal user wants to save text to 	
	 */
	public static void write(String text, String journalName){
		
		try {
			fw = new FileWriter(journal.getAbsoluteFile(), true);
			writer = new BufferedWriter(fw);
			writer.write(text + "/n");
			System.out.println("Appended to journal");
		} 
		catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void add_timedate(){}
}
