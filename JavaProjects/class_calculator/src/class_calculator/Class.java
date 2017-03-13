/**
 * 
 */
package class_calculator;

/**
 * @author anish
 *
 */
public class Class {

	private boolean isWeighted;
	private String instructor;
	private String className;
	private boolean isPowerschool;
	
	
	//COnstructors
	public Class(){
		
		isWeighted = true;
		instructor = " ";
		className = " ";
		isPowerschool = true;
		
	}
	public Class (String name, String teacher, boolean isPowerschool, boolean weighted){
		className = name;
		instructor = teacher;
		isWeighted = weighted;
		
	}
	//Accessing methods
	public String get_className(){
		return className;
	}
	public boolean get_isWeighted(){
		return isWeighted;
	}
	public String get_instructor(){
		return instructor;
	}
	//Modfying methods
	
	public void set_className(String name){
		className = name;
	}
	public void set_isWeighted(boolean weighted){
		isWeighted = weighted;
	}
	public void set_instructor(String teacher){
		instructor = teacher;
	}	
	
	
	
	
	
	
	
	
	
}
