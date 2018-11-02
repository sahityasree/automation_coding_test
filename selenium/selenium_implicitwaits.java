import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;

import org.openqa.selenium.firefox.FirefoxDriver;

public class waits {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.setProperty("webdriver.gecko.driver","C://Users/Admin/Desktop/sahitya/projects/selenium/geckodriver-v0.23.0-win64/geckodriver.exe");
		WebDriver driver= new FirefoxDriver();
		/*
		 * The implicit wait will tell to the web driver to wait for certain amount of time 
		    before it throws a "No Such Element Exception". 
		 * The default setting is 0. Once we set the time, web driver will wait for that 
		   time before throwing an exception.
		 */
		driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS) ;//implicitly wait for 20 seconds
		
		
		
		String eTitle = "Advanced Technology and Data Analytics for Intelligent Commerce - Inmar";
	    String actualTitle = "" ;
		driver.get("https://www.inmar.com/" );
		actualTitle = driver.getTitle();
		System.out.println(actualTitle);
		if (actualTitle.equals(eTitle))
		{
		System.out.println( "Test Passed") ;
		}
		else {
		System.out.println( "Test Failed" );
		}
		
		driver.close();

	}

}
