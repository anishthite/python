/** sets up tobs
 * Saves text user asks to remember, creates running log w/ time
 * @author Anish Thite, December 2016
 * @version 1.1
 * @since 12/20/2016
 */
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
