/*
 Write Selenium script that opens a browser, prints the title of the browser and closes the browser [You may choose the programming
language of your choice]*/

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;


 

public class selenium_openbrowser_title {
	

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		System.setProperty("webdriver.gecko.driver","C://Users/Admin/Desktop/sahitya/projects/selenium/geckodriver-v0.23.0-win64/geckodriver.exe");
		WebDriver driver= new FirefoxDriver();
		driver.get("https://www.synaptics.com");
		String str=driver.getTitle();
		System.out.println(str);
		driver.close();

	}

}
