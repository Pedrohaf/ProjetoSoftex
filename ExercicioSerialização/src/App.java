import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;


public class App {
    public static void main(String[] args) throws Exception {
         arquivoSerializavel();
         lerarquivoserializado();
    }

    private static void arquivoSerializavel(){
        Pessoa p1 = new Pessoa(1 , "Pedro Henrique", 2000, "123456", "Rua Luis Andrade de Sá e Benevides");
        FileOutputStream fos = null;
        ObjectOutputStream oos = null;
        try{
            fos = new FileOutputStream("arquivo.bin");
            oos = new ObjectOutputStream(fos);
            oos.writeObject(p1);
        }catch(FileNotFoundException e){
            System.out.println("Arquivo Não Encontrado.");
        }catch(IOException e){
            System.out.println("Erro ao criar Arquivo");
        }finally{
            try{
                oos.close();
            }catch (IOException e){
                System.out.println("Erro ao Fechar o Arquivo");
            }
        }
            
    }

    private static void lerarquivoserializado(){
        Pessoa p1 = null;
        FileInputStream fis = null;
        ObjectInputStream ois = null;
        try{
            fis = new FileInputStream("arquivo.bin");
            ois = new ObjectInputStream(fis);
            p1 = (Pessoa)ois.readObject();
            System.out.printf("Nome: %s\nEndereço: %s\n", p1.getNome(), p1.getEndereco());
        }catch(ClassNotFoundException e){
            System.out.println("Classe Não Encontrado.");
        }catch(IOException e){
            System.out.println("Erro ao criar Arquivo");
        }finally{
            try{
                ois.close();
            }catch (IOException e){
                System.out.println("Erro ao Fechar o Arquivo");
            }
        }
    }
}
