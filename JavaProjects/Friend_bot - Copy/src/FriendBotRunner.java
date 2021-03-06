import java.util.Scanner;

/**
 * Runner for FriendBot ( original by Laurie While, April 2012)
 * @author Anish Thite
 * @version November 2016
 */
public class FriendBotRunner
{

	/**
	 * Create a friend, give it user input, and print its replies.
	 */
	public static void main(String[] args)
	{
		FriendBot friend = new FriendBot();
		
		System.out.println (friend.getGreeting());
		Scanner in = new Scanner (System.in);
		String statement = in.nextLine();
		
		while (!statement.equals("Bye"))
		{
			System.out.println (friend.getResponse(statement));
			statement = in.nextLine();
		}
	}

}
