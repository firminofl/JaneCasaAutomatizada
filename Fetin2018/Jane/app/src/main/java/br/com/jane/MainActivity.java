package br.com.jane;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import br.com.jane.dao.ConfiguracaoFirebase;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ConfiguracaoFirebase.getFirebase().child("teste").child("-LKtjNwz_x7e7Fr-XHew").setValue("8");
    }
}
