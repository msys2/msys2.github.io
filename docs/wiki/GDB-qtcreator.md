This page is extremely work-in-progress. Eventually it will cover setting up Qt Creator so you can "Start and Debug External Application ..." (you need to build it from source to get access to the latest patch that makes this workable), rebuilding and reinstalling the involved packages in debug, !strip mode and debugging them. The also being able to see Python callstacks and pretty printing of GDB internals in-case you are debugging those sorts of things. For now, this is all I have:

.. To see Python Callstacks and vars when debugging something that intermixes Python and C/C++ (e.g. pygtk)
.. add to .gdbinit or QtCreator Tools->Options->Debugger->GDB->Additional Startup Commands, enter
  python
  sys.path.append('C:/msys64/mingw64/share/gdb/python3')
  import python-gdb
  reload(python-gdb)
  end
