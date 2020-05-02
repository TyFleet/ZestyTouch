using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;
using System.Windows;

public class FoodSearch : MonoBehaviour
{
    public GameObject listFood;

    // Start is called before the first frame update
    void Start() {
        run_cmd(listFood);
    }

    // Update is called once per frame
    void Update() {

    }

    private void run_cmd(GameObject listFood) {

        string fileName = @"PATH_TO_FILE\fillPantry.py {0}", listFood; //Replace with path to python file

        Process p = new Process();
        p.StartInfo = new ProcessStartInfo(@"C:\Python37\python.exe", fileName)
        {
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };
        p.Start();
        string output = p.StandardOutput.ReadToEnd();
        p.WaitForExit();
        Console.WriteLine(output);
        Console.ReadLine();

    } 
}
