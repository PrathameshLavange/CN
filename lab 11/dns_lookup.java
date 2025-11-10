import java.util.*;
import java.net.*;   // ✅ Required for InetAddress & UnknownHostException

public class dns_lookup {
    public static void main(String[] args) {
        String host;
        Scanner ch = new Scanner(System.in);  
        System.out.print("1.Enter Host Name \n2.Enter IP address \nChoice=");
        int choice = ch.nextInt();
        ch.nextLine(); // consume newline left by nextInt()

        if(choice == 1) {  
            System.out.print("\n Enter host name: ");
            host = ch.nextLine();
            try {
                InetAddress address = InetAddress.getByName(host);
                System.out.println("IP address: " + address.getHostAddress());
                System.out.println("Host name : " + address.getHostName()); 
                System.out.println("Host name and IP address: " + address.toString());
            }
            catch (UnknownHostException ex) {
                System.out.println("Could not find " + host);
            }
        }
        else {
            System.out.print("\n Enter IP address: ");
            host = ch.nextLine();
            try {
                InetAddress address = InetAddress.getByName(host);
                System.out.println("Host name : " + address.getHostName());   
                System.out.println("IP address: " + address.getHostAddress());
                System.out.println("Host name and IP address: " + address.toString());
            }
            catch (UnknownHostException ex) {
                System.out.println("Could not find " + host);
            }
        }
    }
}
